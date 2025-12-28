from django.db import models
from django.core.exceptions import ValidationError


class TelegramUser(models.Model):
    """Модель пользователя Telegram"""
    telegram_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Username")
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Фамилия")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name or 'Unknown'} (@{self.username or 'no_username'}) - {self.telegram_id}"


class BotMessage(models.Model):
    """Модель для хранения текстов сообщений бота"""
    MESSAGE_TYPES = [
        ('start', 'Стартовое сообщение'),
        ('about', 'О нас'),
        ('support', 'Поддержка'),
        ('courses', 'Курсы'),
        ('contact', 'Связаться с нами'),
        ('location', 'Как нас найти'),
        ('aml', 'AML Проверка'),
        ('cityex24_question', 'Cityex24 - Вопрос о стране'),
        ('cityex24_contact_request', 'Cityex24 - Запрос контакта'),
        ('cityex24_confirmation', 'Cityex24 - Подтверждение заявки'),
    ]

    message_type = models.CharField(
        max_length=30,
        choices=MESSAGE_TYPES,
        unique=True,
        verbose_name="Тип сообщения"
    )
    text = models.TextField(verbose_name="Текст сообщения")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Сообщение бота"
        verbose_name_plural = "Сообщения бота"
        ordering = ['message_type']

    def __str__(self):
        return dict(self.MESSAGE_TYPES).get(self.message_type, self.message_type)

    @classmethod
    def get_message(cls, message_type):
        """Получить текст сообщения по типу"""
        try:
            return cls.objects.get(message_type=message_type).text
        except cls.DoesNotExist:
            return "Сообщение не настроено"


class ExchangeRate(models.Model):
    """Модель курса обменника"""
    currency_from = models.CharField(max_length=10, verbose_name="Валюта от")
    currency_to = models.CharField(max_length=10, verbose_name="Валюта к")
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Курс обмена"
        verbose_name_plural = "Курсы обмена"
        ordering = ['currency_from', 'currency_to']
        unique_together = [['currency_from', 'currency_to']]

    def __str__(self):
        return f"{self.currency_from} → {self.currency_to}: {self.rate}"

    def clean(self):
        if self.currency_from == self.currency_to:
            raise ValidationError("Валюта 'от' и 'к' не могут быть одинаковыми")


class Cityex24Transfer(models.Model):
    """Модель заявки на международный перевод Cityex24"""
    COUNTRY_CHOICES = [
        ('kyrgyzstan', '🇰🇬 Кыргызстан'),
        ('uzbekistan', '🇺🇿 Узбекистан'),
        ('uae', '🇦🇪 ОАЭ'),
        ('turkey', '🇹🇷 Турция'),
        ('saudi_arabia', '🇸🇦 Саудовская Аравия'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В обработке'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='cityex24_transfers', null=True, blank=True, verbose_name="Пользователь")
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, verbose_name="Страна")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    contact_first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя контакта")
    contact_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фамилия контакта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    notes = models.TextField(blank=True, null=True, verbose_name="Заметки")

    class Meta:
        verbose_name = "Заявка Cityex24"
        verbose_name_plural = "Заявки Cityex24"
        ordering = ['-created_at']

    def __str__(self):
        country_display = dict(self.COUNTRY_CHOICES).get(self.country, self.country)
        return f"{self.user.first_name or 'Unknown'} - {country_display} ({self.get_status_display()})"
    
    def get_country_display_with_flag(self):
        """Получить отображение страны с флагом"""
        return dict(self.COUNTRY_CHOICES).get(self.country, self.country)


class AdminChat(models.Model):
    """Модель для хранения chat_id администраторов для уведомлений"""
    chat_id = models.BigIntegerField(unique=True, verbose_name="Chat ID")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя/Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Chat ID администратора"
        verbose_name_plural = "Chat ID"
        ordering = ['-created_at']

    def __str__(self):
        name_display = f" ({self.name})" if self.name else ""
        status = "✓" if self.is_active else "✗"
        return f"{status} {self.chat_id}{name_display}"
    
    def clean(self):
        """Валидация chat_id"""
        if self.chat_id <= 0:
            raise ValidationError("Chat ID должен быть положительным числом")


class ExchangeOrder(models.Model):
    """Модель заявки на обмен валют"""
    ORDER_TYPE_CHOICES = [
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('processed', 'Обработано'),
        ('cancelled', 'Отменено'),
    ]
    
    telegram_user_id = models.BigIntegerField(null=True, blank=True, verbose_name="Telegram User ID")
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES, verbose_name="Тип заявки")
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Сумма")
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс обмена")
    amount_to_receive = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Сумма к получению")
    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О")
    wallet_address = models.CharField(max_length=255, verbose_name="Адрес кошелька")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    notes = models.TextField(blank=True, null=True, verbose_name="Заметки")

    class Meta:
        verbose_name = "Заявка на обмен"
        verbose_name_plural = "Заявки на обмен"
        ordering = ['-created_at']

    def __str__(self):
        order_type_display = dict(self.ORDER_TYPE_CHOICES).get(self.order_type, self.order_type)
        return f"#{self.id} - {order_type_display} - {self.full_name} ({self.get_status_display()})"

