#!/bin/bash
# Скрипт для запуска локального бэкенда с доступом извне

echo "Запуск Django сервера на 0.0.0.0:8000..."
echo "Для доступа из интернета используйте ngrok: ngrok http 8000"
echo ""

python3 manage.py runserver 0.0.0.0:8000

