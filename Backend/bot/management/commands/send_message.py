from django.core.management.base import BaseCommand
from bot.models import TelegramUser
from bot.bot import send_broadcast_message


class Command(BaseCommand):
    help = 'Отправить сообщение всем пользователям бота'

    def add_arguments(self, parser):
        parser.add_argument('message', type=str, help='Текст сообщения для отправки')

    def handle(self, *args, **options):
        message = options['message']
        users = TelegramUser.objects.all()
        count = users.count()
        
        self.stdout.write(f'Отправка сообщения {count} пользователям...')
        
        success_count = 0
        error_count = 0
        
        for user in users:
            try:
                send_broadcast_message(user.telegram_id, message)
                success_count += 1
            except Exception as e:
                error_count += 1
                self.stdout.write(self.style.ERROR(f'Ошибка отправки пользователю {user.telegram_id}: {e}'))
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Отправлено успешно: {success_count}, Ошибок: {error_count}'
            )
        )

