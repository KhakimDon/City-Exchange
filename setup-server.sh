#!/bin/bash
# Скрипт для первоначальной настройки сервера
# Запустите этот скрипт на сервере один раз для настройки

set -e

echo "🚀 Настройка сервера City Exchange..."

# Обновление системы
echo "📦 Обновление системы..."
apt update && apt upgrade -y

# Установка необходимых пакетов
echo "📦 Установка зависимостей..."
apt install -y python3 python3-pip python3-venv git nginx bun curl

# Установка gunicorn для продакшена
echo "📦 Установка gunicorn..."
pip3 install gunicorn

# Создание директории для проекта
echo "📁 Создание директорий..."
mkdir -p /opt/city-exchange
mkdir -p /var/www/city-exchange

# Клонирование репозитория (если еще не клонирован)
if [ ! -d "/opt/city-exchange/.git" ]; then
    echo "📥 Клонирование репозитория..."
    read -p "Введите URL вашего GitHub репозитория: " REPO_URL
    git clone $REPO_URL /opt/city-exchange
fi

# Настройка Backend
echo "⚙️ Настройка Backend..."
cd /opt/city-exchange/Backend

# Создание виртуального окружения
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Создание .env файла если его нет
if [ ! -f ".env" ]; then
    echo "📝 Создание .env файла..."
    cat > .env << 'ENVFILE'
SECRET_KEY=change-this-to-secure-key-in-production
DEBUG=False
ALLOWED_HOSTS=178.72.149.8,localhost,127.0.0.1
TELEGRAM_BOT_TOKEN=your-bot-token-here
TELEGRAM_NOTIFICATION_BOT_TOKEN=your-notification-bot-token-here
TELEGRAM_ADMIN_CHAT_ID=your-admin-chat-id-here
DATABASE_URL=sqlite:///db.sqlite3
ENVFILE
    echo "⚠️  ВАЖНО: Отредактируйте /opt/city-exchange/Backend/.env и добавьте ваши токены!"
fi

# Миграции
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Настройка Frontend
echo "⚙️ Настройка Frontend..."
cd /opt/city-exchange/Frontend

if command -v bun &> /dev/null; then
    bun install
    bun run build
else
    npm install
    npm run build
fi

# Копирование фронтенда
cp -r dist/* /var/www/city-exchange/

# Создание systemd сервисов
echo "⚙️ Создание systemd сервисов..."

# Backend сервис
cat > /tmp/city-exchange-backend.service << 'SERVICE'
[Unit]
Description=City Exchange Django Backend
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/city-exchange/Backend
Environment="PATH=/opt/city-exchange/Backend/venv/bin"
ExecStart=/opt/city-exchange/Backend/venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
SERVICE

sudo mv /tmp/city-exchange-backend.service /etc/systemd/system/

# Bot сервис
cat > /tmp/city-exchange-bot.service << 'SERVICE'
[Unit]
Description=City Exchange Telegram Bot
After=network.target city-exchange-backend.service

[Service]
Type=simple
User=root
WorkingDirectory=/opt/city-exchange/Backend
Environment="PATH=/opt/city-exchange/Backend/venv/bin"
ExecStart=/opt/city-exchange/Backend/venv/bin/python manage.py run_bot
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
SERVICE

sudo mv /tmp/city-exchange-bot.service /etc/systemd/system/

# Перезагрузка systemd и запуск сервисов
echo "🔄 Запуск сервисов..."
sudo systemctl daemon-reload
sudo systemctl enable city-exchange-backend
sudo systemctl enable city-exchange-bot
sudo systemctl start city-exchange-backend
sudo systemctl start city-exchange-bot

# Настройка Nginx (опционально)
echo "🌐 Настройка Nginx..."
cat > /tmp/city-exchange-nginx.conf << 'NGINX'
server {
    listen 80;
    server_name 178.72.149.8;

    # Frontend
    location / {
        root /var/www/city-exchange;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Admin panel
    location /admin/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
NGINX

sudo mv /tmp/city-exchange-nginx.conf /etc/nginx/sites-available/city-exchange
sudo ln -sf /etc/nginx/sites-available/city-exchange /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx || echo "⚠️  Nginx не настроен, проверьте конфигурацию"

echo ""
echo "✅ Настройка завершена!"
echo ""
echo "📊 Статус сервисов:"
sudo systemctl status city-exchange-backend --no-pager -l
echo ""
sudo systemctl status city-exchange-bot --no-pager -l
echo ""
echo "🌐 Backend доступен на: http://178.72.149.8:8000"
echo "🌐 Frontend доступен на: http://178.72.149.8"
echo ""
echo "⚠️  ВАЖНО: Отредактируйте /opt/city-exchange/Backend/.env и добавьте ваши токены!"

