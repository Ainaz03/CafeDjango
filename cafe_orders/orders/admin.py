from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Настройки админ-панели для управления заказами.
    """
    list_display = ('id', 'table_number', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('table_number', 'status')
    ordering = ('-id',)
