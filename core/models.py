from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} : <{self.quantity}>"


class Order(models.Model):
    # User =
    order_products = models.ManyToManyField(OrderProduct)
    ordered_datetime = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)
