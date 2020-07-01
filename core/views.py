from django.views.generic import TemplateView, ListView, DetailView

from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, reverse, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone


from . import models
from . import forms

from djangostore import settings


# public views
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO
        return context


class ProductDetailView(DetailView):
    template_name = "core/product_detail.html"
    model = models.Product


class ProductListView(ListView):
    template_name = "core/product_list.html"
    model = models.Product


# Private view

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "core/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CartView(LoginRequiredMixin, TemplateView):
    # TemplateView
    template_name = "core/cart.html"

    # LoginRequiredMixin
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        orders_for_user = models.Order.objects.filter(
            user=user.id).filter(is_ordered=False)
        if orders_for_user.exists():
            context['order_products'] = orders_for_user[0].order_products.all()
        return context


class CheckoutView(LoginRequiredMixin, View):
    # TemplateView
    template_name = "core/checkout.html"

    # LoginRequiredMixin
    login_url = settings.LOGIN_URL

    def get(self, request):
        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request):
        pass


class AddProductToCart(LoginRequiredMixin, View):
    # LoginRequiredMixin
    login_url = settings.LOGIN_URL

    def post(self, request, pk):
        user = request.user
        # TODO parse quantity from form
        try:
            product = models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            return HttpResponseNotFound()

        form = forms.AddToCart(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # Check if there are orders/cart
            orders_for_user = models.Order.objects.filter(
                user=user.id).filter(is_ordered=False)
            if not orders_for_user.exists():
                # else create OrderItem and order
                op = models.OrderProduct(
                    user=user, product=product, quantity=quantity)
                op.save()
                order = models.Order(
                    user=user, ordered_datetime=timezone.now())
                order.save()
                order.order_products.add(op)
            else:
                # Get the order that is_order=False (ie cart)
                # Check if there order items with the same product, if add the number to order item
                # else create OrderItem and order
                cart = orders_for_user[0]
                qs = cart.order_products.filter(product__id=pk)
                if qs.exists():
                    op = qs[0]
                    # order product already in cart
                    op.quantity += quantity
                    op.save()
                else:
                    # create new product order and update cart
                    op = models.OrderProduct(
                        user=user, product=product, quantity=quantity)
                    op.save()
                    cart.order_products.add(op)

            return redirect(reverse('cart'))
        else:
            return redirect(reverse('products-detail', args=[pk]))


class RemoveProductFromCart(LoginRequiredMixin, View):
    # LoginRequiredMixin
    login_url = settings.LOGIN_URL

    def post(self, request, pk):
        user = request.user
        try:
            product = models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            return HttpResponseNotFound()

        orders_for_user = models.Order.objects.filter(
            user=user.id).filter(is_ordered=False)
        if not orders_for_user.exists():
            return HttpResponseNotFound()
        else:
            cart = orders_for_user[0]
            qs = cart.order_products.filter(product__id=pk)
            if qs.exists():
                op = qs[0]
                op.delete()
            else:
                return HttpResponseNotFound()
        return redirect(reverse('cart'))
