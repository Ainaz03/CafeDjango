from typing import Union
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from .models import Order
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Список заказов + поиск
def order_list(request: HttpRequest) -> HttpResponse:
    """
    Получает список заказов с возможностью поиска по номеру стола или статусу.
    """
    query: str = request.GET.get("query", "").strip()
    orders = Order.objects.all()

    if query:
        if query.isdigit():
            orders = orders.filter(table_number=int(query))
        else:
            orders = orders.filter(status__icontains=query)

    return render(request, 'orders/list.html', {'orders': orders})


# Создание заказа
def create_order(request: HttpRequest) -> Union[HttpResponse, HttpResponse]:
    """
    Создаёт новый заказ. Проверяет корректность данных.
    """
    if request.method == "POST":
        table_number = request.POST.get("table_number")
        items = request.POST.get("items")
        total_price = request.POST.get("total_price")

        if not table_number or not items or not total_price:
            return render(request, "orders/create_order.html", {"error": "Все поля обязательны!"})

        try:
            table_number = int(table_number)
            total_price = float(total_price)
        except ValueError:
            return render(request, "orders/create_order.html", {"error": "Некорректные данные!"})

        Order.objects.create(
            table_number=table_number,
            items=items,
            total_price=total_price,
            status="waiting"
        )

        return redirect("order_list")

    return render(request, "orders/create_order.html")


# Удаление заказа
def delete_order(request: HttpRequest, order_id: int) -> HttpResponse:
    """
    Удаляет заказ, если он существует.
    """
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect(reverse('order_list'))


# Обновление статуса заказа
def update_order_status(request: HttpRequest, order_id: int) -> HttpResponse:
    """
    Обновляет статус заказа, если переданы корректные данные.
    """
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        valid_statuses = [choice[0] for choice in Order.STATUS_CHOICES]

        if new_status not in valid_statuses:
            return render(request, "orders/update_status.html", {"order": order, "error": "Некорректный статус!"})

        order.status = new_status
        order.save()

    return redirect(reverse('order_list') + f'?query={order.table_number}')


# Расчёт выручки за смену
def daily_revenue(request: HttpRequest) -> HttpResponse:
    """
    Подсчитывает сумму оплаченных заказов за день.
    """
    revenue = Order.objects.filter(status="paid").aggregate(total=Sum("total_price"))["total"] or 0
    return render(request, 'orders/revenue.html', {'revenue': revenue})


# API: Получение списка заказов
@api_view(['GET'])
def api_orders(request: HttpRequest) -> Response:
    """
    API-эндпоинт для получения списка заказов в JSON-формате.
    """
    orders = Order.objects.values("id", "table_number", "items", "total_price", "status")
    return Response(list(orders))
