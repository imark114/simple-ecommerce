from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentListView,
    PaymentDetailView,
)

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
] 