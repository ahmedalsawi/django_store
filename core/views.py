from django.views.generic import TemplateView, ListView, DetailView

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from djangostore import settings


# Private views
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    template_name = "core/product_detail.html"
    model = models.Product


class ProductListView(ListView):
    template_name = "core/product_list.html"
    model = models.Product


# Private views

class CartView(LoginRequiredMixin, TemplateView):
    # TemplateView
    template_name = "core/cart.html"

    # LoginRequiredMixin
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
