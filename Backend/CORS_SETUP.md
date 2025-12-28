# Настройка CORS для работы с Netlify

## Проблема
Запросы с фронтенда на Netlify (jocular-squirrel-8dd574.netlify.app) не проходят к бэкенду.

## Решение

### 1. Обновите ALLOWED_HOSTS в settings.py
Добавьте домен вашего бэкенда в ALLOWED_HOSTS:

```python
ALLOWED_HOSTS = ['your-backend-domain.com', 'localhost', '127.0.0.1']
```

### 2. CORS уже настроен
В settings.py уже добавлен домен Netlify в CORS_ALLOWED_ORIGINS:
- `https://jocular-squirrel-8dd574.netlify.app`

### 3. Настройте переменную окружения на фронтенде
Создайте файл `.env` в папке Frontend с URL вашего бэкенда:

```
VITE_API_BASE_URL=https://your-backend-domain.com
```

Или если бэкенд на том же домене, но другом порту:
```
VITE_API_BASE_URL=https://jocular-squirrel-8dd574.netlify.app:8000
```

### 4. Для продакшена
Если бэкенд размещен отдельно, убедитесь что:
- Бэкенд доступен по HTTPS
- ALLOWED_HOSTS содержит домен бэкенда
- CORS_ALLOWED_ORIGINS содержит домен Netlify

### 5. Проверка
После настройки проверьте в консоли браузера:
- Нет ли ошибок CORS
- Правильно ли формируются URL запросов
- Доступен ли бэкенд по указанному адресу

## Пример настройки для разных хостингов

### Если бэкенд на Railway/Render/Heroku:
```python
ALLOWED_HOSTS = ['your-app.railway.app', 'your-app.onrender.com']
```

### Если бэкенд на отдельном сервере:
```python
ALLOWED_HOSTS = ['api.yourdomain.com', 'yourdomain.com']
```

