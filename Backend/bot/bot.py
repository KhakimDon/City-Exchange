import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from django.conf import settings
from asgiref.sync import sync_to_async
from bot.models import TelegramUser, BotMessage, ExchangeRate, Cityex24Transfer, AdminChat, ExchangeOrder

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


@sync_to_async
def get_or_create_user(update: Update) -> TelegramUser:
    """Получить или создать пользователя"""
    user_data = update.effective_user
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=user_data.id,
        defaults={
            'username': user_data.username,
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
        }
    )
    if not created:
        # Обновить данные пользователя
        user.username = user_data.username
        user.first_name = user_data.first_name
        user.last_name = user_data.last_name
        user.save()
    return user


def get_main_keyboard():
    """Создать главную клавиатуру"""
    keyboard = [
        [
            KeyboardButton("О нас"),
            KeyboardButton("Курсы"),
        ],
        [
            KeyboardButton("AML Проверка"),
            KeyboardButton("Связаться с нами"),
        ],
        [
            KeyboardButton("Как нас найти"),
        ],
        [
            KeyboardButton("Международные переводы Cityex24"),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_countries_keyboard():
    """Создать клавиатуру с выбором стран"""
    keyboard = [
        [
            KeyboardButton("🇰🇬 Кыргызстан"),
            KeyboardButton("🇺🇿 Узбекистан"),
        ],
        [
            KeyboardButton("🇦🇪 ОАЭ"),
            KeyboardButton("🇹🇷 Турция"),
        ],
        [
            KeyboardButton("🇸🇦 Саудовская Аравия"),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_contact_keyboard():
    """Создать клавиатуру с кнопкой запроса контакта"""
    keyboard = [
        [
            KeyboardButton("Поделиться контактом", request_contact=True),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)


@sync_to_async
def get_start_message():
    """Получить стартовое сообщение"""
    try:
        return BotMessage.objects.get(message_type='start').text
    except BotMessage.DoesNotExist:
        return "Добро пожаловать в City Exchange! Выберите нужный раздел:"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    try:
        logger.info(f"Получена команда /start от пользователя {update.effective_user.id}")
        user = await get_or_create_user(update)
        logger.info(f"Пользователь получен/создан: {user.telegram_id}")
        
        start_message = await get_start_message()
        logger.info(f"Стартовое сообщение получено: {start_message[:50]}...")
        
        if not start_message or start_message == "Сообщение не настроено":
            start_message = "Добро пожаловать в City Exchange! Выберите нужный раздел:"
        
        await update.message.reply_text(
            start_message,
            reply_markup=get_main_keyboard()
        )
        logger.info("Стартовое сообщение отправлено успешно")
    except Exception as e:
        logger.error(f"Ошибка в обработчике start: {e}", exc_info=True)
        try:
            await update.message.reply_text(
                "Добро пожаловать в City Exchange! Выберите нужный раздел:",
                reply_markup=get_main_keyboard()
            )
        except Exception as e2:
            logger.error(f"Критическая ошибка при отправке сообщения: {e2}")


@sync_to_async
def get_bot_message(message_type):
    """Получить сообщение бота по типу"""
    try:
        return BotMessage.objects.get(message_type=message_type).text
    except BotMessage.DoesNotExist:
        return "Сообщение не настроено"

@sync_to_async
def get_exchange_rates():
    """Получить активные курсы обмена"""
    return list(ExchangeRate.objects.filter(is_active=True))

@sync_to_async
def create_cityex24_transfer(user, country_text):
    """Создать заявку Cityex24"""
    country_map = {
        "🇰🇬 Кыргызстан": "kyrgyzstan",
        "🇺🇿 Узбекистан": "uzbekistan",
        "🇦🇪 ОАЭ": "uae",
        "🇹🇷 Турция": "turkey",
        "🇸🇦 Саудовская Аравия": "saudi_arabia",
    }
    country_code = country_map.get(country_text)
    if not country_code:
        return None
    
    transfer = Cityex24Transfer.objects.create(
        user=user,
        country=country_code,
        status='new'
    )
    return transfer

@sync_to_async
def save_contact_to_transfer(transfer_id, phone_number, first_name=None, last_name=None):
    """Сохранить контакт в заявку"""
    try:
        transfer = Cityex24Transfer.objects.get(pk=transfer_id)
        transfer.contact_phone = phone_number
        transfer.contact_first_name = first_name
        transfer.contact_last_name = last_name
        transfer.save()
        return transfer
    except Cityex24Transfer.DoesNotExist:
        return None

async def handle_country_selection(update: Update, context: ContextTypes.DEFAULT_TYPE, country_text: str):
    """Обработать выбор страны"""
    try:
        user = await get_or_create_user(update)
        transfer = await create_cityex24_transfer(user, country_text)
        
        if transfer:
            # Сохраняем ID заявки в контексте для последующего сохранения контакта
            context.user_data['pending_transfer_id'] = transfer.id
            
            # Отправляем запрос контакта
            contact_request_message = await get_bot_message('cityex24_contact_request')
            if contact_request_message == "Сообщение не настроено":
                contact_request_message = "Укажите контакты для обратной связи"
            
            await update.message.reply_text(
                contact_request_message,
                reply_markup=get_contact_keyboard()
            )
        else:
            await update.message.reply_text(
                "Произошла ошибка при создании заявки. Попробуйте позже.",
                reply_markup=get_main_keyboard()
            )
    except Exception as e:
        logger.error(f"Ошибка при обработке выбора страны: {e}", exc_info=True)
        await update.message.reply_text(
            "Произошла ошибка. Пожалуйста, попробуйте позже.",
            reply_markup=get_main_keyboard()
        )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    try:
        text = update.message.text
        user = await get_or_create_user(update)
        
        if text == "О нас":
            message = await get_bot_message('about')
            if message == "Сообщение не настроено":
                message = "Информация о нас скоро будет добавлена."
            await update.message.reply_text(message, reply_markup=get_main_keyboard())
        
        elif text == "Курсы":
            rates = await get_exchange_rates()
            courses_text = await get_bot_message('courses')
            
            if rates:
                message = ""
                if courses_text and courses_text != "Сообщение не настроено":
                    message = f"{courses_text}\n\n"
                message += "📊 Актуальные курсы обмена:\n\n"
                for rate in rates:
                    message += f"💱 {rate.currency_from} → {rate.currency_to}: {rate.rate}\n"
            else:
                message = courses_text if courses_text != "Сообщение не настроено" else "Курсы обмена скоро будут добавлены."
            await update.message.reply_text(message, reply_markup=get_main_keyboard())
        
        elif text == "AML Проверка":
            message = await get_bot_message('aml')
            if message == "Сообщение не настроено":
                message = "Информация об AML проверке скоро будет добавлена."
            await update.message.reply_text(message, reply_markup=get_main_keyboard())
        
        elif text == "Связаться с нами":
            message = await get_bot_message('contact')
            if message == "Сообщение не настроено":
                message = "Контактная информация скоро будет добавлена."
            await update.message.reply_text(message, reply_markup=get_main_keyboard())
        
        elif text == "Как нас найти":
            message = await get_bot_message('location')
            if message == "Сообщение не настроено":
                message = "Информация о местоположении скоро будет добавлена."
            await update.message.reply_text(message, reply_markup=get_main_keyboard())
        
        elif text == "Международные переводы Cityex24":
            message = await get_bot_message('cityex24_question')
            if message == "Сообщение не настроено":
                message = "В какую страну нужно перевести деньги? По международным переводам работаем с 08:00 до 20:00 по МСК"
            await update.message.reply_text(message, reply_markup=get_countries_keyboard())
        
        # Обработка выбора стран
        elif text in ["🇰🇬 Кыргызстан", "🇺🇿 Узбекистан", "🇦🇪 ОАЭ", "🇹🇷 Турция", "🇸🇦 Саудовская Аравия"]:
            await handle_country_selection(update, context, text)
        
        else:
            await update.message.reply_text(
                "Пожалуйста, используйте кнопки меню для навигации.",
                reply_markup=get_main_keyboard()
            )
    except Exception as e:
        logger.error(f"Ошибка в обработчике handle_text: {e}")
        await update.message.reply_text(
            "Произошла ошибка. Пожалуйста, попробуйте позже.",
            reply_markup=get_main_keyboard()
        )


async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработать получение контакта от пользователя"""
    try:
        contact = update.message.contact
        if not contact:
            return
        
        # Получаем ID заявки из контекста
        transfer_id = context.user_data.get('pending_transfer_id')
        if not transfer_id:
            await update.message.reply_text(
                "Произошла ошибка. Пожалуйста, начните заново.",
                reply_markup=get_main_keyboard()
            )
            return
        
        # Сохраняем контакт
        transfer = await save_contact_to_transfer(
            transfer_id=transfer_id,
            phone_number=contact.phone_number,
            first_name=contact.first_name,
            last_name=contact.last_name
        )
        
        if transfer:
            # Отправляем подтверждение
            confirmation_message = await get_bot_message('cityex24_confirmation')
            if confirmation_message == "Сообщение не настроено":
                confirmation_message = "Ваша заявка принята, скоро менеджер свяжется с вами"
            
            await update.message.reply_text(
                confirmation_message,
                reply_markup=get_main_keyboard()
            )
            
            # Очищаем контекст
            context.user_data.pop('pending_transfer_id', None)
            
            # Отправляем уведомление в другой бот
            await send_notification_to_admin(transfer)
        else:
            await update.message.reply_text(
                "Произошла ошибка при сохранении контакта. Попробуйте позже.",
                reply_markup=get_main_keyboard()
            )
    except Exception as e:
        logger.error(f"Ошибка при обработке контакта: {e}", exc_info=True)
        await update.message.reply_text(
            "Произошла ошибка. Пожалуйста, попробуйте позже.",
            reply_markup=get_main_keyboard()
        )


@sync_to_async
def get_active_admin_chats():
    """Получить список активных chat_id администраторов"""
    return list(AdminChat.objects.filter(is_active=True).values_list('chat_id', flat=True))

@sync_to_async
def get_transfer_data(transfer):
    """Получить данные заявки для уведомления"""
    # Загружаем связанные объекты
    transfer = Cityex24Transfer.objects.select_related('user').get(pk=transfer.pk)
    country_display = transfer.get_country_display_with_flag()
    
    # Формируем информацию о пользователе
    if transfer.user:
        user_info = f"{transfer.user.first_name or ''} {transfer.user.last_name or ''}".strip()
        if not user_info:
            user_info = f"@{transfer.user.username}" if transfer.user.username else f"ID: {transfer.user.telegram_id}"
    else:
        # Если пользователь не указан, используем информацию из контакта
        contact_name = f"{transfer.contact_first_name or ''} {transfer.contact_last_name or ''}".strip()
        user_info = contact_name if contact_name else "Веб-заявка"
    
    # Формируем информацию о контакте
    contact_info = ""
    if transfer.contact_phone:
        contact_name = f"{transfer.contact_first_name or ''} {transfer.contact_last_name or ''}".strip()
        if contact_name:
            contact_info = f"{contact_name}\n📱 {transfer.contact_phone}"
        else:
            contact_info = f"📱 {transfer.contact_phone}"
    
    return {
        'country_display': country_display,
        'user_info': user_info,
        'created_at': transfer.created_at,
        'transfer_id': transfer.id,
        'contact_info': contact_info
    }

async def send_notification_to_admin(transfer):
    """Отправить уведомление о новой заявке в админский бот на все активные chat_id"""
    try:
        from telegram import Bot
        
        logger.info("Начало отправки уведомления о новой заявке")
        
        if not settings.TELEGRAM_NOTIFICATION_BOT_TOKEN:
            logger.error("TELEGRAM_NOTIFICATION_BOT_TOKEN не установлен в настройках")
            return
        
        logger.info(f"Токен бота уведомлений установлен: {settings.TELEGRAM_NOTIFICATION_BOT_TOKEN[:20]}...")
        
        # Получаем данные заявки
        transfer_data = await get_transfer_data(transfer)
        
        # Инициализируем бота
        notification_bot = Bot(token=settings.TELEGRAM_NOTIFICATION_BOT_TOKEN)
        await notification_bot.initialize()
        
        message = f"🔔 Новая заявка Cityex24\n\n"
        message += f"👤 Пользователь: {transfer_data['user_info']}\n"
        message += f"🌍 Страна: {transfer_data['country_display']}\n"
        if transfer_data['contact_info']:
            message += f"📞 Контакт: {transfer_data['contact_info']}\n"
        message += f"📅 Дата: {transfer_data['created_at'].strftime('%d.%m.%Y %H:%M')}\n"
        message += f"🆔 ID заявки: {transfer_data['transfer_id']}"
        
        logger.info(f"Текст уведомления подготовлен: {message[:100]}...")
        
        # Получаем список активных chat_id из базы данных
        admin_chat_ids = await get_active_admin_chats()
        logger.info(f"Найдено активных chat_id: {len(admin_chat_ids)} - {admin_chat_ids}")
        
        if admin_chat_ids:
            success_count = 0
            error_count = 0
            for chat_id in admin_chat_ids:
                try:
                    logger.info(f"Попытка отправить уведомление на chat_id: {chat_id}")
                    await notification_bot.send_message(chat_id=int(chat_id), text=message)
                    success_count += 1
                    logger.info(f"✓ Уведомление успешно отправлено администратору (chat_id: {chat_id})")
                except Exception as e:
                    error_count += 1
                    error_msg = str(e)
                    logger.error(f"✗ Ошибка при отправке уведомления администратору (chat_id: {chat_id}): {error_msg}")
                    logger.error(f"  Тип ошибки: {type(e).__name__}")
                    # Проверяем специфичные ошибки
                    if "chat not found" in error_msg.lower() or "chat_id is empty" in error_msg.lower():
                        logger.error(f"  ВНИМАНИЕ: Пользователь с chat_id {chat_id} не начал диалог с ботом-уведомлений!")
                    elif "unauthorized" in error_msg.lower():
                        logger.error(f"  ВНИМАНИЕ: Неверный токен бота или бот заблокирован!")
            
            logger.info(f"Итог отправки уведомлений: успешно {success_count}, ошибок {error_count}")
        else:
            logger.warning("Нет активных chat_id администраторов для отправки уведомлений. Добавьте chat_id в админке!")
        
        await notification_bot.shutdown()
    except Exception as e:
        logger.error(f"Критическая ошибка при отправке уведомления: {e}", exc_info=True)

async def send_exchange_order_notification(order):
    """Отправить уведомление о новой заявке на обмен в админский бот на все активные chat_id"""
    try:
        from telegram import Bot
        
        logger.info("Начало отправки уведомления о новой заявке на обмен")
        
        if not settings.TELEGRAM_NOTIFICATION_BOT_TOKEN:
            logger.error("TELEGRAM_NOTIFICATION_BOT_TOKEN не установлен в настройках")
            return
        
        logger.info(f"Токен бота уведомлений установлен: {settings.TELEGRAM_NOTIFICATION_BOT_TOKEN[:20]}...")
        
        # Инициализируем бота
        notification_bot = Bot(token=settings.TELEGRAM_NOTIFICATION_BOT_TOKEN)
        await notification_bot.initialize()
        
        # Формируем сообщение
        order_type_display = "Покупка" if order.order_type == 'buy' else "Продажа"
        
        # Форматируем суммы с 2 знаками после запятой
        amount_formatted = f"{order.amount:.2f}".replace('.', ',')
        amount_to_receive_formatted = f"{order.amount_to_receive:.2f}".replace('.', ',')
        exchange_rate_formatted = f"{order.exchange_rate:.4f}".replace('.', ',')
        
        # Формируем строку с Telegram ID (если есть)
        telegram_id_str = f"👤 Telegram ID: {order.telegram_user_id}\n" if order.telegram_user_id else ""
        
        message = f"🔔 Новая транзакция на обмен\n\n"
        message += f"🆔 Номер заявки: #{order.id}\n"
        message += f"📋 Тип: {order_type_display}\n"
        message += f"💰 Сумма: {amount_formatted} {'RUB' if order.order_type == 'buy' else 'USDT'}\n"
        message += f"💱 Курс: {exchange_rate_formatted}\n"
        message += f"💵 К получению: {amount_to_receive_formatted} {'USDT' if order.order_type == 'buy' else 'RUB'}\n"
        message += f"👤 Ф.И.О: {order.full_name}\n"
        message += f"🔗 Адрес кошелька: {order.wallet_address}\n"
        message += telegram_id_str
        message += f"📅 Дата: {order.created_at.strftime('%d.%m.%Y %H:%M')}\n"
        message += f"📊 Статус: {order.get_status_display()}"
        
        logger.info(f"Текст уведомления подготовлен: {message[:100]}...")
        
        # Получаем список активных chat_id из базы данных
        admin_chat_ids = await get_active_admin_chats()
        logger.info(f"Найдено активных chat_id: {len(admin_chat_ids)} - {admin_chat_ids}")
        
        if admin_chat_ids:
            success_count = 0
            error_count = 0
            for chat_id in admin_chat_ids:
                try:
                    logger.info(f"Попытка отправить уведомление на chat_id: {chat_id}")
                    await notification_bot.send_message(chat_id=int(chat_id), text=message)
                    success_count += 1
                    logger.info(f"✓ Уведомление успешно отправлено администратору (chat_id: {chat_id})")
                except Exception as e:
                    error_count += 1
                    error_msg = str(e)
                    logger.error(f"✗ Ошибка при отправке уведомления администратору (chat_id: {chat_id}): {error_msg}")
                    logger.error(f"  Тип ошибки: {type(e).__name__}")
                    # Проверяем специфичные ошибки
                    if "chat not found" in error_msg.lower() or "chat_id is empty" in error_msg.lower():
                        logger.error(f"  ВНИМАНИЕ: Пользователь с chat_id {chat_id} не начал диалог с ботом-уведомлений!")
                    elif "unauthorized" in error_msg.lower():
                        logger.error(f"  ВНИМАНИЕ: Неверный токен бота или бот заблокирован!")
            
            logger.info(f"Итог отправки уведомлений: успешно {success_count}, ошибок {error_count}")
        else:
            logger.warning("Нет активных chat_id администраторов для отправки уведомлений. Добавьте chat_id в админке!")
        
        await notification_bot.shutdown()
    except Exception as e:
        logger.error(f"Критическая ошибка при отправке уведомления о заявке на обмен: {e}", exc_info=True)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    logger.error(f"Update {update} caused error {context.error}")


def send_broadcast_message(telegram_id: int, message: str):
    """Отправить сообщение пользователю (для использования в админке)"""
    from telegram import Bot
    import asyncio
    
    async def _send():
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        try:
            await bot.send_message(chat_id=telegram_id, text=message, reply_markup=get_main_keyboard())
            return True
        except Exception as e:
            logger.error(f"Ошибка отправки сообщения пользователю {telegram_id}: {e}")
            return False
        finally:
            await bot.close()
    
    try:
        return asyncio.run(_send())
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения: {e}")
        return False


def run_polling():
    """Запустить бота в режиме polling"""
    if not settings.TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN не установлен в настройках")
    
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_error_handler(error_handler)
    
    logger.info("Бот запущен и готов к работе")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

