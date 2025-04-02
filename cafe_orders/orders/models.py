from django.db import models
from typing import Dict, Any, List


class Order(models.Model):
    """Модель заказа в кафе."""

    STATUS_CHOICES = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.IntegerField(verbose_name="Номер стола")
    items = models.TextField(verbose_name="Список блюд")  # Можно заменить на JSONField, если используешь PostgreSQL
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость", default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting', verbose_name="Статус")

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return f"Заказ {self.id} (Стол {self.table_number}) - {self.get_status_display()}"

    def update_order(self, data: Dict[str, Any]) -> bool:
        """
        Обновляет заказ, если переданы корректные данные.
        
        :param data: Словарь с новыми значениями полей.
        :return: True, если заказ обновлен, иначе False.
        """
        allowed_fields = {'table_number', 'items', 'total_price', 'status'}
        updated = False

        for key, value in data.items():
            if key in allowed_fields and hasattr(self, key):
                setattr(self, key, value)
                updated = True

        if updated:
            self.save()
        return updated

    @classmethod
    def get_orders_by_status(cls, status: str) -> List["Order"]:
        """
        Получает список заказов по статусу.

        :param status: Статус заказа (waiting, ready, paid).
        :return: Список заказов.
        """
        return list(cls.objects.filter(status=status))
