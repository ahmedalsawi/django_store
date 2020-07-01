from django.urls import path, include

from . import views

#app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(),
         name='products-list'),
    path('products/<pk>/', views.ProductDetailView.as_view(),
         name='products-detail'),
    path('profile/', views.ProfileView.as_view(),
         name='profile'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<pk>/', views.AddProductToCart.as_view(), name='cart-add'),
    path('cart/remove/<pk>/',
         views.RemoveProductFromCart.as_view(), name='cart-remove'),
    path('cart/checkout/', views.CheckoutView.as_view(),
         name='cart-checkout'),
]
