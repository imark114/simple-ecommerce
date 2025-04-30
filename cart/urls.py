from django.urls import path
from .views import (
    CartView,
    CartItemCreateView,
    CartItemUpdateView,
    CartItemDeleteView,
)

urlpatterns = [
    path('shopping-cart/', CartView.as_view(), name='cart-detail'),
    path('shopping-cart/items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('shopping-cart/items/<int:pk>/', CartItemUpdateView.as_view(), name='cart-item-update'),
    path('shopping-cart/items/<int:pk>/remove/', CartItemDeleteView.as_view(), name='cart-item-delete'),
] 