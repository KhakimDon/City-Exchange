# Решение проблемы с ngrok предупреждением (ERR_NGROK_6024)

## Проблема
При обращении к ngrok URL появляется страница с предупреждением:
"You are about to visit ... This website is served for free through ngrok.com"

## Решение

### Вариант 1: Добавить заголовок в запросы (Рекомендуется)

Обновите `Frontend/src/services/api.ts` чтобы добавлять заголовок `ngrok-skip-browser-warning`:

```typescript
private async request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  const url = `${this.baseURL}${endpoint}`
  const config: RequestInit = {
    headers: {
      'Content-Type': 'application/json',
      'ngrok-skip-browser-warning': 'true',  // Пропускает предупреждение
      ...options.headers
    },
    ...options
  }
  // ... остальной код
}
```

### Вариант 2: Использовать платную версию ngrok
Платная версия не показывает предупреждение.

### Вариант 3: Зарегистрировать бесплатный аккаунт ngrok
1. Зарегистрируйтесь на https://ngrok.com/
2. Получите authtoken
3. Настройте: `ngrok config add-authtoken YOUR_TOKEN`
4. Используйте фиксированный домен (платно) или просто авторизуйтесь (может помочь)

### Вариант 4: Использовать альтернативы
- **localtunnel**: `npm install -g localtunnel && lt --port 8000`
- **serveo**: `ssh -R 80:localhost:8000 serveo.net`
- **cloudflared**: `cloudflared tunnel --url http://localhost:8000`

## Важно
Это предупреждение не блокирует работу API - запросы проходят, просто браузер показывает предупреждение. Для API запросов из JavaScript это не проблема, если добавить заголовок.

