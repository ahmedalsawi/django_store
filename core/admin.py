from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from . import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.OrderProduct)
admin.site.register(models.Order)

admin.site.register(models.User, UserAdmin)
