from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from orders.models import Order
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentListView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    swagger_tags = ['payments']

    @swagger_auto_schema(
        operation_description="Get all payments for current user",
        responses={200: PaymentSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new payment",
        request_body=PaymentSerializer,
        responses={201: PaymentSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        return Payment.objects.filter(order__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    swagger_tags = ['payments']

    @swagger_auto_schema(
        operation_description="Get payment details",
        responses={200: PaymentSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Payment.objects.filter(order__user=self.request.user)
