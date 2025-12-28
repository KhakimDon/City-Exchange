# Настройка для разработки Telegram Mini App

## Вариант 1: Использование ngrok (Рекомендуется)

### 1. Установка ngrok

```bash
# Через Homebrew
brew install ngrok/ngrok/ngrok

# Или скачайте с https://ngrok.com/download
```

### 2. Регистрация и получение токена

1. Зарегистрируйтесь на https://ngrok.com (бесплатно)
2. Получите токен авторизации
3. Авторизуйтесь:
```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

### 3. Запуск локального сервера

```bash
cd Frontend
bun run dev
# Сервер запустится на http://localhost:3000
```

### 4. Создание HTTPS туннеля

В новом терминале:
```bash
ngrok http 3000
```

Вы получите HTTPS URL вида: `https://xxxx-xx-xxx-xxx-xx.ngrok-free.app`

### 5. Настройка бота в BotFather

1. Откройте [@BotFather](https://t.me/BotFather) в Telegram
2. Отправьте команду `/newbot` или выберите существующего бота
3. Отправьте команду `/newapp` или `/editapp`
4. Выберите бота
5. Укажите URL вашего приложения: `https://xxxx-xx-xxx-xxx-xx.ngrok-free.app`
6. Укажите название и описание приложения

### 6. Тестирование

1. Откройте вашего бота в Telegram
2. Нажмите на кнопку "Open App" или отправьте команду `/start`
3. Приложение должно открыться в Telegram

## Вариант 2: Использование Cloudflare Tunnel (Альтернатива)

```bash
# Установка
brew install cloudflare/cloudflare/cloudflared

# Запуск туннеля
cloudflared tunnel --url http://localhost:3000
```

## Вариант 3: Использование локального HTTPS с mkcert

### 1. Установка mkcert

```bash
brew install mkcert
brew install nss # для Firefox
```

### 2. Создание локального CA

```bash
mkcert -install
```

### 3. Генерация сертификатов

```bash
cd Frontend
mkcert localhost 127.0.0.1 ::1 10.246.22.36
# Это создаст файлы: localhost+3.pem и localhost+3-key.pem
```

### 4. Обновление vite.config.ts

```typescript
import fs from 'fs'

export default defineConfig({
  // ...
  server: {
    https: {
      key: fs.readFileSync('./localhost+3-key.pem'),
      cert: fs.readFileSync('./localhost+3.pem'),
    },
    port: 3000,
    host: true
  }
})
```

## Важные замечания

1. **HTTPS обязателен**: Telegram требует HTTPS для Mini Apps
2. **ngrok URL меняется**: При каждом перезапуске ngrok URL меняется (в бесплатной версии)
3. **Для продакшена**: Используйте реальный домен с SSL сертификатом
4. **Telegram Test Servers**: Можно использовать для тестирования без публичного URL

## Быстрый старт с ngrok

```bash
# Терминал 1: Запуск dev сервера
cd Frontend
bun run dev

# Терминал 2: Запуск ngrok
ngrok http 3000

# Скопируйте HTTPS URL из ngrok и используйте в BotFather
```

