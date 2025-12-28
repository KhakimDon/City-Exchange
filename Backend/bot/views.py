from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import json
from decimal import Decimal, InvalidOperation
from bot.models import TelegramUser, ExchangeOrder, ExchangeRate, Cityex24Transfer, BotMessage
from bot.bot import send_broadcast_message
import asyncio
from bot.bot import send_exchange_order_notification, send_notification_to_admin


@csrf_exempt
@require_http_methods(["POST"])
def create_exchange_order(request):
    """API endpoint для создания заявки на обмен"""
    try:
        data = json.loads(request.body)
        
        # Валидация обязательных полей
        required_fields = ['order_type', 'amount', 'exchange_rate', 'full_name', 'wallet_address']
        for field in required_fields:
            if field not in data:
                return JsonResponse({
                    'success': False,
                    'error': f'Поле {field} обязательно для заполнения'
                }, status=400)
        
        # Валидация типа заявки
        if data['order_type'] not in ['buy', 'sell']:
            return JsonResponse({
                'success': False,
                'error': 'Тип заявки должен быть "buy" или "sell"'
            }, status=400)
        
        # Валидация и преобразование числовых значений
        try:
            amount = Decimal(str(data['amount']))
            exchange_rate = Decimal(str(data['exchange_rate']))
            
            if amount <= 0:
                return JsonResponse({
                    'success': False,
                    'error': 'Сумма должна быть больше нуля'
                }, status=400)
            
            if exchange_rate <= 0:
                return JsonResponse({
                    'success': False,
                    'error': 'Курс обмена должен быть больше нуля'
                }, status=400)
            
            # Расчет суммы к получению
            if data['order_type'] == 'sell':
                # Продажа USDT за рубли: amount * rate
                amount_to_receive = amount * exchange_rate
            else:
                # Покупка USDT за рубли: amount / rate
                amount_to_receive = amount / exchange_rate
            
        except (InvalidOperation, ValueError, TypeError) as e:
            return JsonResponse({
                'success': False,
                'error': 'Неверный формат числовых значений'
            }, status=400)
        
        # Валидация ФИО
        if not data['full_name'].strip():
            return JsonResponse({
                'success': False,
                'error': 'Ф.И.О не может быть пустым'
            }, status=400)
        
        # Валидация адреса кошелька (базовая проверка TRC-20)
        wallet_address = data['wallet_address'].strip()
        if not wallet_address:
            return JsonResponse({
                'success': False,
                'error': 'Адрес кошелька не может быть пустым'
            }, status=400)
        
        # Создание заявки
        order = ExchangeOrder.objects.create(
            telegram_user_id=data.get('telegram_user_id'),
            order_type=data['order_type'],
            amount=amount,
            exchange_rate=exchange_rate,
            amount_to_receive=amount_to_receive,
            full_name=data['full_name'].strip(),
            wallet_address=wallet_address,
            status='pending'
        )
        
        # Отправка уведомления в Telegram бот
        try:
            asyncio.run(send_exchange_order_notification(order))
        except Exception as e:
            # Логируем ошибку, но не прерываем создание заявки
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Ошибка при отправке уведомления о заявке {order.id}: {e}")
        
        return JsonResponse({
            'success': True,
            'order_id': order.id,
            'order': {
                'id': order.id,
                'order_type': order.order_type,
                'amount': str(order.amount),
                'exchange_rate': str(order.exchange_rate),
                'amount_to_receive': str(order.amount_to_receive),
                'full_name': order.full_name,
                'wallet_address': order.wallet_address,
                'status': order.status,
                'created_at': order.created_at.isoformat(),
            }
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Неверный формат JSON'
        }, status=400)
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка при создании заявки: {e}", exc_info=True)
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def create_cityex24_transfer(request):
    """API endpoint для создания заявки Cityex24"""
    try:
        data = json.loads(request.body)
        
        # Валидация обязательных полей
        required_fields = ['country', 'contact_phone']
        for field in required_fields:
            if field not in data:
                return JsonResponse({
                    'success': False,
                    'error': f'Поле {field} обязательно для заполнения'
                }, status=400)
        
        # Валидация страны
        valid_countries = ['kyrgyzstan', 'uzbekistan', 'uae', 'turkey', 'saudi_arabia']
        if data['country'] not in valid_countries:
            return JsonResponse({
                'success': False,
                'error': 'Неверная страна'
            }, status=400)
        
        # Валидация телефона
        contact_phone = data['contact_phone'].strip()
        if not contact_phone:
            return JsonResponse({
                'success': False,
                'error': 'Телефон не может быть пустым'
            }, status=400)
        
        # Получаем или создаем пользователя Telegram (если telegram_user_id передан)
        user = None
        telegram_user_id = data.get('telegram_user_id')
        if telegram_user_id:
            user, created = TelegramUser.objects.get_or_create(
                telegram_id=telegram_user_id,
                defaults={
                    'first_name': data.get('contact_first_name', ''),
                    'last_name': data.get('contact_last_name', ''),
                }
            )
            if not created:
                # Обновляем данные пользователя если они переданы
                if data.get('contact_first_name'):
                    user.first_name = data.get('contact_first_name')
                if data.get('contact_last_name'):
                    user.last_name = data.get('contact_last_name')
                user.save()
        
        # Создание заявки
        transfer = Cityex24Transfer.objects.create(
            user=user,
            country=data['country'],
            contact_phone=contact_phone,
            contact_first_name=data.get('contact_first_name', ''),
            contact_last_name=data.get('contact_last_name', ''),
            status='new'
        )
        
        # Отправка уведомления в Telegram бот
        try:
            asyncio.run(send_notification_to_admin(transfer))
        except Exception as e:
            # Логируем ошибку, но не прерываем создание заявки
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Ошибка при отправке уведомления о заявке Cityex24 {transfer.id}: {e}")
        
        return JsonResponse({
            'success': True,
            'transfer_id': transfer.id,
            'transfer': {
                'id': transfer.id,
                'country': transfer.country,
                'contact_phone': transfer.contact_phone,
                'contact_first_name': transfer.contact_first_name,
                'contact_last_name': transfer.contact_last_name,
                'status': transfer.status,
                'created_at': transfer.created_at.isoformat(),
            }
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Неверный формат JSON'
        }, status=400)
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка при создании заявки Cityex24: {e}", exc_info=True)
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)


@csrf_exempt
@require_http_methods(["GET"])
def get_exchange_rates(request):
    """API endpoint для получения активных курсов обмена"""
    try:
        # Получаем активные курсы
        rates = ExchangeRate.objects.filter(is_active=True)
        
        # Формируем ответ
        rates_data = []
        for rate in rates:
            rates_data.append({
                'currency_from': rate.currency_from,
                'currency_to': rate.currency_to,
                'rate': str(rate.rate),
            })
        
        return JsonResponse({
            'success': True,
            'rates': rates_data
        }, status=200)
        
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка при получении курсов: {e}", exc_info=True)
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)


@csrf_exempt
@require_http_methods(["GET"])
def get_user_orders(request):
    """API endpoint для получения заявок пользователя"""
    try:
        # Получаем telegram_user_id из query параметров
        telegram_user_id = request.GET.get('telegram_user_id')
        
        if not telegram_user_id:
            return JsonResponse({
                'success': False,
                'error': 'telegram_user_id обязателен'
            }, status=400)
        
        try:
            telegram_user_id = int(telegram_user_id)
        except ValueError:
            return JsonResponse({
                'success': False,
                'error': 'Неверный формат telegram_user_id'
            }, status=400)
        
        # Получаем заявки пользователя
        orders = ExchangeOrder.objects.filter(telegram_user_id=telegram_user_id).order_by('-created_at')
        
        # Формируем ответ
        orders_data = []
        for order in orders:
            orders_data.append({
                'id': order.id,
                'order_type': order.order_type,
                'order_type_display': order.get_order_type_display(),
                'amount': str(order.amount),
                'exchange_rate': str(order.exchange_rate),
                'amount_to_receive': str(order.amount_to_receive),
                'full_name': order.full_name,
                'wallet_address': order.wallet_address,
                'status': order.status,
                'status_display': order.get_status_display(),
                'created_at': order.created_at.isoformat(),
                'updated_at': order.updated_at.isoformat(),
            })
        
        return JsonResponse({
            'success': True,
            'orders': orders_data
        }, status=200)
        
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка при получении заявок пользователя: {e}", exc_info=True)
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)


@csrf_exempt
@require_http_methods(["GET"])
def get_bot_message(request):
    """API endpoint для получения текста сообщения бота по типу"""
    try:
        # Получаем message_type из query параметров
        message_type = request.GET.get('message_type')
        
        if not message_type:
            return JsonResponse({
                'success': False,
                'error': 'message_type обязателен'
            }, status=400)
        
        # Проверяем, что тип сообщения существует в списке допустимых
        valid_types = [choice[0] for choice in BotMessage.MESSAGE_TYPES]
        if message_type not in valid_types:
            return JsonResponse({
                'success': False,
                'error': f'Неверный тип сообщения. Допустимые типы: {", ".join(valid_types)}'
            }, status=400)
        
        # Получаем сообщение
        try:
            bot_message = BotMessage.objects.get(message_type=message_type)
            return JsonResponse({
                'success': True,
                'text': bot_message.text
            }, status=200)
        except BotMessage.DoesNotExist:
            return JsonResponse({
                'success': True,
                'text': 'Сообщение не настроено'
            }, status=200)
        
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка при получении сообщения бота: {e}", exc_info=True)
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)

