from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products', views.ProductListView.as_view(),
         name='product-list'),
    path('product/<pk>/', views.ProductDetailView.as_view(),
         name='product-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('addtocart/<pk>/', views.AddProductToCart.as_view(), name='add-to-cart'),
    path('removefromcart/<pk>/', views.RemoveProductFromCart.as_view(),
         name='remove-from-cart'),
    path('checkout/', views.CheckoutView.as_view(),
         name='checkout'),
    path('profile/', views.ProfileView.as_view(),
         name='profile'),
]
