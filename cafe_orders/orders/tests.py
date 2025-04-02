from django.test import TestCase
from django.urls import reverse
from .models import Order

class OrderTestCase(TestCase):
    def setUp(self):
        """
        Подготовка тестовых данных: создание тестового заказа.
        """
        self.order = Order.objects.create(
            table_number=5,
            items="Пицца, Салат",
            total_price=750,
            status="waiting"
        )

    def test_order_creation(self):
        """
        Проверка корректности создания заказа.
        """
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(self.order.status, "waiting")

    def test_order_list_view(self):
        """
        Проверка отображения списка заказов.
        """
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пицца, Салат")

    def test_order_deletion(self):
        """
        Проверка удаления заказа.
        """
        response = self.client.post(reverse('delete_order', args=[self.order.id]))
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(response.status_code, 302)  # Редирект

    def test_order_update_status(self):
        """
        Проверка обновления статуса заказа.
        """
        response = self.client.post(reverse('update_status', args=[self.order.id]), {'status': 'ready'})
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "ready")
        self.assertEqual(response.status_code, 302)  # Редирект

    def test_daily_revenue(self):
        """
        Проверка расчёта дневной выручки.
        """
        self.order.status = "paid"
        self.order.save()
        response = self.client.get(reverse('daily_revenue'))
        self.assertContains(response, "750")

    def test_api_orders(self):
        """
        Проверка API-эндпоинта списка заказов.
        """
        response = self.client.get(reverse('api_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
