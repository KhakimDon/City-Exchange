# Настройка Telegram Mini App

## Шаги для запуска проекта в Telegram Mini App

### 1. Сборка проекта

```bash
bun install
bun run build
```

После сборки файлы будут в папке `dist/`

### 2. Деплой на хостинг

Загрузите содержимое папки `dist/` на любой статический хостинг:
- Vercel
- Netlify
- GitHub Pages
- Cloudflare Pages
- Или любой другой статический хостинг

**Важно:** Хостинг должен поддерживать HTTPS!

### 3. Настройка бота в Telegram

1. Создайте бота через [@BotFather](https://t.me/BotFather)
2. Отправьте команду `/newapp`
3. Выберите вашего бота
4. Укажите название Mini App
5. Укажите URL вашего задеплоенного приложения (например: `https://your-domain.com`)
6. Загрузите иконку (опционально)
7. Загрузите изображение для превью (опционально)

### 4. Тестирование

1. Откройте вашего бота в Telegram
2. Нажмите на кнопку "Menu" или команду `/start`
3. Mini App должен открыться

### 5. Локальная разработка

Для локальной разработки используйте:

```bash
bun run dev
```

Затем используйте [ngrok](https://ngrok.com/) или [localtunnel](https://localtunnel.github.io/www/) для создания HTTPS туннеля:

```bash
# С ngrok
ngrok http 3000

# С localtunnel
npx localtunnel --port 3000
```

Используйте полученный HTTPS URL в настройках бота для тестирования.

## Использование Telegram API в компонентах

```vue
<script setup lang="ts">
import { useTelegram } from '@/composables/useTelegram'
import { useTelegramStore } from '@/stores/telegram'

const { WebApp, showAlert, close } = useTelegram()
const telegramStore = useTelegramStore()

// Получить данные пользователя
const user = telegramStore.user

// Показать алерт
showAlert('Привет из Mini App!')

// Закрыть приложение
// close()
</script>
```

## Основные возможности

- `useTelegram()` - composable для работы с Telegram WebApp API
- `useTelegramStore()` - Pinia store с данными пользователя и настройками
- Автоматическая инициализация при загрузке
- Поддержка темной/светлой темы
- Доступ к данным пользователя

