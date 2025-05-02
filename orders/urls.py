from django.urls import path
from .views import (
    OrderListView,
    OrderDetailView,
    OrderItemView,
    UserOrdersView,
)

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:order_id>/items/', OrderItemView.as_view(), name='order-item-list'),
    path('user/<int:user_id>/', UserOrdersView.as_view(), name='user-orders'),
] 