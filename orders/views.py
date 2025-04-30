from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderCreateSerializer
from cart.models import Cart, CartItem

# Create your views here.

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user, is_active=True)
        order = serializer.save(user=self.request.user)
        
        # Create order items from cart items
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
        
        # Deactivate the cart
        cart.is_active = False
        cart.save()

class OrderUpdateView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
