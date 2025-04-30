from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'total_price']
        read_only_fields = ['price', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user', 'total_price', 'status']

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(user=self.context['request'].user)
        
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price
            
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )
        
        return order 