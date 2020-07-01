from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, User

from djangostore import settings


class User(AbstractUser):
    user_avatar = models.ImageField(upload_to="uploads", blank=True)


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("products-detail", kwargs={
    #         'pk': self.id
    #     })

    # def get_add_to_cart_url(self):
    #     return reverse("cart-add", kwargs={
    #         'pk': self.id
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("cart-remove", kwargs={
    #         'pk': self.id
    #     })


class OrderProduct(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
    order_products = models.ManyToManyField(OrderProduct)
    ordered_datetime = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order owner:{self.user.username}"

    def get_total(self):
        total = 0
        for order_item in self.order_products.all():
            total += order_item.get_total_item_price()
        return total
