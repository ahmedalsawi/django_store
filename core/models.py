from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, User

from djangostore import settings


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()


class OrderProduct(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} : <{self.quantity}>"


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
    order_products = models.ManyToManyField(OrderProduct)
    ordered_datetime = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)
