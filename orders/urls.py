from django.urls import path
from .views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
)

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
] 