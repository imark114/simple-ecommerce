from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from orders.models import Order

# Create your views here.

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order_id = self.request.data.get('order')
        order = Order.objects.get(id=order_id, user=self.request.user)
        
        # In a real application, you would integrate with a payment gateway here
        # For now, we'll just create the payment record
        payment = serializer.save(
            user=self.request.user,
            amount=order.total_price,
            status='completed'  # In a real app, this would depend on the payment gateway response
        )
        
        # Update order payment status
        order.payment_status = True
        order.save()

class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
