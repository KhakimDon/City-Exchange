# GitHub Actions Workflows

Этот проект использует GitHub Actions для автоматизации CI/CD процессов.

## Доступные Workflows

### 1. Backend CI (`backend-ci.yml`)
- **Триггер**: Push/PR в ветки main, master, develop при изменении Backend/
- **Что делает**:
  - Устанавливает Python 3.11
  - Устанавливает зависимости
  - Запускает миграции БД
  - Проверяет код Django (`python manage.py check`)
  - Запускает тесты (если есть)

### 2. Frontend CI (`frontend-ci.yml`)
- **Триггер**: Push/PR в ветки main, master, develop при изменении Frontend/
- **Что делает**:
  - Устанавливает Bun
  - Устанавливает зависимости
  - Запускает линтер
  - Проверяет типы TypeScript
  - Собирает проект
  - Сохраняет артефакты сборки

### 3. Deploy (`deploy.yml`)
- **Триггер**: Push в main/master или ручной запуск
- **Что делает**:
  - Подключается к серверу по SSH
  - Обновляет код из репозитория
  - Деплоит Backend (устанавливает зависимости, миграции, collectstatic)
  - Деплоит Frontend (собирает проект)

## Настройка Secrets

Для работы workflow `deploy.yml` нужно добавить Secrets в настройках репозитория GitHub:

1. Перейдите в **Settings** → **Secrets and variables** → **Actions**
2. Добавьте следующие secrets:

   - `SERVER_HOST` - IP адрес или домен сервера (например: `178.72.149.8`)
   - `SERVER_USER` - пользователь для SSH (например: `root`)
   - `SERVER_SSH_KEY` - приватный SSH ключ для подключения к серверу
   - `REPO_URL` - URL вашего репозитория (например: `https://github.com/username/city-exchange.git`)

## Как получить SSH ключ для сервера

Если у вас уже есть SSH ключ на сервере, используйте его. Или создайте новый:

```bash
ssh-keygen -t ed25519 -C "github-actions" -f ~/.ssh/id_ed25519_github
```

Затем добавьте публичный ключ на сервер:
```bash
ssh-copy-id -i ~/.ssh/id_ed25519_github.pub root@178.72.149.8
```

И приватный ключ добавьте в GitHub Secrets как `SERVER_SSH_KEY`.

## Бесплатные лимиты GitHub Actions

- **Публичные репозитории**: неограниченно бесплатно
- **Приватные репозитории**: 
  - 2000 минут/месяц бесплатно
  - Дополнительные минуты можно купить

## Автозапуск сервисов

После деплоя сервисы **автоматически запускаются** через systemd:

- **Backend (Django)**: `city-exchange-backend.service` - запускается на порту 8000
- **Bot (Telegram)**: `city-exchange-bot.service` - запускается автоматически

### Первоначальная настройка сервера

Для первого раза запустите на сервере скрипт настройки:

```bash
# На сервере
cd /opt/city-exchange
wget https://raw.githubusercontent.com/your-username/city-exchange/main/setup-server.sh
chmod +x setup-server.sh
sudo ./setup-server.sh
```

Или скопируйте `setup-server.sh` на сервер и запустите его.

### Управление сервисами вручную

```bash
# Проверить статус
sudo systemctl status city-exchange-backend
sudo systemctl status city-exchange-bot

# Перезапустить
sudo systemctl restart city-exchange-backend
sudo systemctl restart city-exchange-bot

# Остановить
sudo systemctl stop city-exchange-backend
sudo systemctl stop city-exchange-bot

# Посмотреть логи
sudo journalctl -u city-exchange-backend -f
sudo journalctl -u city-exchange-bot -f
```

## Отключение workflows

Если нужно временно отключить workflows, просто закомментируйте их в файлах `.yml` или удалите файлы из `.github/workflows/`.

