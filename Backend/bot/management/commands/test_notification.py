from django.core.management.base import BaseCommand
from bot.models import AdminChat, Cityex24Transfer
from bot.bot import send_notification_to_admin
import asyncio


class Command(BaseCommand):
    help = 'Тестовая отправка уведомления администраторам'

    def add_arguments(self, parser):
        parser.add_argument('--chat-id', type=int, help='Chat ID для тестовой отправки (опционально)')

    def handle(self, *args, **options):
        self.stdout.write('Тестовая отправка уведомления...')
        
        # Получаем последнюю заявку или создаем тестовую
        try:
            transfer = Cityex24Transfer.objects.last()
            if not transfer:
                self.stdout.write(self.style.ERROR('Нет заявок в базе данных. Создайте заявку через бота.'))
                return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при получении заявки: {e}'))
            return
        
        # Если указан chat_id, используем его
        if options.get('chat_id'):
            chat_id = options['chat_id']
            self.stdout.write(f'Отправка тестового уведомления на chat_id: {chat_id}')
            # Временно создаем тестовый chat_id
            admin_chat, created = AdminChat.objects.get_or_create(
                chat_id=chat_id,
                defaults={'name': 'Тестовый', 'is_active': True}
            )
            if not admin_chat.is_active:
                admin_chat.is_active = True
                admin_chat.save()
        
        # Проверяем активные chat_id
        active_chats = AdminChat.objects.filter(is_active=True)
        if not active_chats.exists():
            self.stdout.write(self.style.WARNING('Нет активных chat_id в базе данных!'))
            self.stdout.write('Добавьте chat_id в админке: /admin/bot/adminchat/')
            return
        
        self.stdout.write(f'Найдено активных chat_id: {active_chats.count()}')
        for chat in active_chats:
            self.stdout.write(f'  - {chat.chat_id} ({chat.name or "без имени"})')
        
        # Отправляем уведомление
        try:
            asyncio.run(send_notification_to_admin(transfer))
            self.stdout.write(self.style.SUCCESS('Уведомление отправлено! Проверьте логи для деталей.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при отправке: {e}'))

