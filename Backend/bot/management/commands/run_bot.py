from django.core.management.base import BaseCommand
from bot.bot import run_polling


class Command(BaseCommand):
    help = 'Запустить Telegram бота'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Запуск Telegram бота...'))
        try:
            run_polling()
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Бот остановлен пользователем'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при запуске бота: {e}'))

