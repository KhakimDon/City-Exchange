from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse, path
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.admin.helpers import AdminForm
from django.forms.formsets import formset_factory
from .models import TelegramUser, BotMessage, ExchangeRate, Cityex24Transfer, AdminChat, ExchangeOrder
from .bot import send_broadcast_message


class SendMessageForm(forms.Form):
    """Форма для отправки сообщений"""
    message = forms.CharField(
        label='Текст сообщения',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80, 'class': 'vLargeTextField'}),
        required=True,
        help_text='Введите текст сообщения, которое будет отправлено пользователям'
    )
    
    class Media:
        css = {
            'all': ('admin/css/widgets.css',)
        }


class SendMessageModelAdmin(admin.ModelAdmin):
    """Временный ModelAdmin для отображения формы отправки сообщений"""
    pass


def send_message_view(request):
    """Представление для отправки сообщений используя стандартные шаблоны Django admin"""
    user_ids = request.session.get('selected_user_ids', [])
    user_count = len(user_ids) if user_ids else TelegramUser.objects.count()
    is_selected = bool(user_ids)
    
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message_text = form.cleaned_data['message'].strip()
            
            if not user_ids:
                # Отправить всем пользователям
                users = TelegramUser.objects.all()
                user_ids = list(users.values_list('telegram_id', flat=True))
            
            success_count = 0
            error_count = 0
            
            for telegram_id in user_ids:
                if send_broadcast_message(telegram_id, message_text):
                    success_count += 1
                else:
                    error_count += 1
            
            messages.success(
                request,
                f'Сообщение отправлено: успешно {success_count}, ошибок {error_count}'
            )
            
            # Очистить сессию
            if 'selected_user_ids' in request.session:
                del request.session['selected_user_ids']
            
            return redirect('admin:bot_telegramuser_changelist')
    else:
        form = SendMessageForm()
    
    # Используем стандартные шаблоны Django admin
    opts = TelegramUser._meta
    model_admin = SendMessageModelAdmin(TelegramUser, admin.site)
    
    # Создаем AdminForm для использования стандартных шаблонов
    fieldsets = (
        ('Отправить сообщение пользователям', {
            'fields': ('message',),
            'description': mark_safe(f'Сообщение будет отправлено <strong>{"выбранным" if is_selected else "всем"}</strong> пользователям ({user_count}).' if user_count else 'Сообщение будет отправлено всем пользователям.')
        }),
    )
    
    admin_form = AdminForm(
        form,
        fieldsets,
        {},
        model_admin=model_admin,
    )
    
    # Подготовка контекста для стандартного шаблона Django admin
    context = admin.site.each_context(request)
    
    # Добавляем все необходимые переменные для шаблона
    context.update({
        'title': 'Отправить сообщение пользователям',
        'admin_form': admin_form,
        'form': form,
        'opts': opts,
        'model_admin': model_admin,
        'has_view_permission': True,
        'has_add_permission': False,
        'has_change_permission': False,
        'has_delete_permission': False,
        'has_absolute_url': False,
        'original': None,
        'is_popup': False,
        'is_popup_var': '_popup',
        'show_delete': False,
        'show_save': True,
        'save_as': False,
        'show_save_and_continue': False,
        'show_save_and_add_another': False,
        'add': False,
        'change': False,
        'save_on_top': False,
        'has_editable_inline_admin_formsets': False,
        'inline_admin_formsets': [],
        'inline_admin_formset_errors': [],
        'errors': form.errors if not form.is_valid() else None,
        'non_field_errors': form.non_field_errors(),
        'media': form.media,
        'user_count': user_count,
        'is_selected': is_selected,
    })
    
    # Используем стандартный шаблон Django admin для форм
    return render(request, 'admin/change_form.html', context)


# Расширяем AdminSite для добавления кастомного URL
original_get_urls = admin.site.get_urls

def get_urls():
    """Добавляем кастомный URL в админку"""
    from django.urls import path
    urls = [
        path('bot/send-message/', admin.site.admin_view(send_message_view), name='bot_send_message'),
    ]
    return urls + original_get_urls()

admin.site.get_urls = get_urls


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'first_name', 'last_name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['telegram_id', 'username', 'first_name', 'last_name']
    readonly_fields = ['telegram_id', 'created_at', 'updated_at']
    actions = ['send_message_to_selected', 'send_message_to_all']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('telegram_id', 'username', 'first_name', 'last_name')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def send_message_to_selected(self, request, queryset):
        """Отправить сообщение выбранным пользователям"""
        # Сохраняем выбранные ID в сессии
        user_ids = list(queryset.values_list('telegram_id', flat=True))
        request.session['selected_user_ids'] = user_ids
        
        # Перенаправляем на страницу ввода сообщения
        return HttpResponseRedirect(reverse('admin:bot_send_message'))
    
    send_message_to_selected.short_description = 'Отправить сообщение выбранным пользователям'

    def send_message_to_all(self, request, queryset):
        """Отправить сообщение всем пользователям"""
        # Очищаем сессию, чтобы отправить всем
        if 'selected_user_ids' in request.session:
            del request.session['selected_user_ids']
        
        # Перенаправляем на страницу ввода сообщения
        return HttpResponseRedirect(reverse('admin:bot_send_message'))
    
    send_message_to_all.short_description = 'Отправить сообщение'


@admin.register(BotMessage)
class BotMessageAdmin(admin.ModelAdmin):
    list_display = ['message_type_display', 'text_preview', 'updated_at']
    list_filter = ['message_type', 'updated_at']
    search_fields = ['text']
    readonly_fields = ['updated_at']
    
    fieldsets = (
        ('Настройка сообщения', {
            'fields': ('message_type', 'text')
        }),
        ('Информация', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )

    def message_type_display(self, obj):
        return dict(BotMessage.MESSAGE_TYPES).get(obj.message_type, obj.message_type)
    message_type_display.short_description = 'Тип сообщения'

    def text_preview(self, obj):
        preview = obj.text[:100] + '...' if len(obj.text) > 100 else obj.text
        return format_html('<span style="color: #666;">{}</span>', preview)
    text_preview.short_description = 'Предпросмотр текста'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    actions = ['send_test_message']

    def send_test_message(self, request, queryset):
        """Отправить тестовое сообщение (заглушка)"""
        count = queryset.count()
        self.message_user(
            request,
            f'Функция отправки тестового сообщения будет реализована в боте.'
        )
    send_test_message.short_description = 'Отправить тестовое сообщение'


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['currency_from', 'currency_to', 'rate', 'is_active', 'updated_at']
    list_filter = ['is_active', 'currency_from', 'currency_to', 'updated_at']
    search_fields = ['currency_from', 'currency_to']
    list_editable = ['is_active', 'rate']
    
    fieldsets = (
        ('Курс обмена', {
            'fields': ('currency_from', 'currency_to', 'rate', 'is_active')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs


@admin.register(Cityex24Transfer)
class Cityex24TransferAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_display', 'country_display', 'contact_display', 'status', 'created_at']
    list_filter = ['status', 'country', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'user__telegram_id', 'contact_phone']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Информация о заявке', {
            'fields': ('user', 'country', 'status')
        }),
        ('Контактная информация', {
            'fields': ('contact_phone', 'contact_first_name', 'contact_last_name')
        }),
        ('Дополнительная информация', {
            'fields': ('notes',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def user_display(self, obj):
        if not obj.user:
            return format_html('<span style="color: #999;">Не указан</span>')
        user_info = f"{obj.user.first_name or ''} {obj.user.last_name or ''}".strip()
        if not user_info:
            user_info = f"@{obj.user.username}" if obj.user.username else f"ID: {obj.user.telegram_id}"
        return format_html('<strong>{}</strong>', user_info)
    user_display.short_description = 'Пользователь'
    
    def country_display(self, obj):
        return obj.get_country_display_with_flag()
    country_display.short_description = 'Страна'
    
    def contact_display(self, obj):
        if obj.contact_phone:
            contact_name = f"{obj.contact_first_name or ''} {obj.contact_last_name or ''}".strip()
            if contact_name:
                return format_html('<strong>{}</strong><br>📱 {}', contact_name, obj.contact_phone)
            return format_html('📱 {}', obj.contact_phone)
        return format_html('<span style="color: #999;">Не указан</span>')
    contact_display.short_description = 'Контакт'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')


@admin.register(AdminChat)
class AdminChatAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['chat_id', 'name']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Информация', {
            'fields': ('chat_id', 'name', 'is_active')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs


@admin.register(ExchangeOrder)
class ExchangeOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_type_display', 'amount_display', 'exchange_rate', 'amount_to_receive_display', 'full_name', 'status', 'created_at']
    list_filter = ['status', 'order_type', 'created_at']
    search_fields = ['id', 'full_name', 'wallet_address', 'telegram_user_id']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('telegram_user_id', 'order_type', 'status')
        }),
        ('Финансовая информация', {
            'fields': ('amount', 'exchange_rate', 'amount_to_receive')
        }),
        ('Информация о пользователе', {
            'fields': ('full_name', 'wallet_address')
        }),
        ('Дополнительная информация', {
            'fields': ('notes',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def order_type_display(self, obj):
        return dict(ExchangeOrder.ORDER_TYPE_CHOICES).get(obj.order_type, obj.order_type)
    order_type_display.short_description = 'Тип заявки'
    
    def amount_display(self, obj):
        currency = 'RUB' if obj.order_type == 'buy' else 'USDT'
        return f"{obj.amount} {currency}"
    amount_display.short_description = 'Сумма'
    
    def amount_to_receive_display(self, obj):
        currency = 'USDT' if obj.order_type == 'buy' else 'RUB'
        return f"{obj.amount_to_receive} {currency}"
    amount_to_receive_display.short_description = 'К получению'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

