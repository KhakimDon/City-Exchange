from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from bot.models import ExchangeOrder
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Отменяет заявки на обмен, которые не были обработаны в течение 4 часов'

    def handle(self, *args, **options):
        # Вычисляем время 4 часа назад
        four_hours_ago = timezone.now() - timedelta(hours=4)
        
        # Находим заявки со статусом "Ожидание", созданные более 4 часов назад
        expired_orders = ExchangeOrder.objects.filter(
            status='pending',
            created_at__lt=four_hours_ago
        )
        
        count = expired_orders.count()
        
        if count > 0:
            # Обновляем статус на "Отменено"
            expired_orders.update(status='cancelled', updated_at=timezone.now())
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Успешно отменено {count} заявок, которые не были обработаны в течение 4 часов'
                )
            )
            logger.info(f'Отменено {count} заявок, которые не были обработаны в течение 4 часов')
        else:
            self.stdout.write(
                self.style.SUCCESS('Нет заявок для отмены')
            )

