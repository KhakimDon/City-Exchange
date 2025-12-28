"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bot.views import create_exchange_order, create_cityex24_transfer, get_exchange_rates, get_user_orders, get_bot_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', create_exchange_order, name='create_exchange_order'),
    path('api/orders/user/', get_user_orders, name='get_user_orders'),
    path('api/cityex24/', create_cityex24_transfer, name='create_cityex24_transfer'),
    path('api/exchange-rates/', get_exchange_rates, name='get_exchange_rates'),
    path('api/bot-message/', get_bot_message, name='get_bot_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

