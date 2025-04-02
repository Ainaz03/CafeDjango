from django.urls import path
from .views import (
    order_list, create_order, delete_order,
    update_order_status, daily_revenue, api_orders
)

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='create_order'),
    path('delete/<int:order_id>/', delete_order, name='delete_order'),
    path('update_status/<int:order_id>/', update_order_status, name='update_status'),
    path('revenue/', daily_revenue, name='daily_revenue'),
    path('api/orders/', api_orders, name='api_orders'),
]
