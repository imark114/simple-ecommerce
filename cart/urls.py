from django.urls import path
from .views import (
    CartView,
    CartItemView,
    CartItemDetailView,
    UserCartView,
)

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('items/', CartItemView.as_view(), name='cart-item-list'),
    path('items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('user/<int:user_id>/', UserCartView.as_view(), name='user-cart'),
] 