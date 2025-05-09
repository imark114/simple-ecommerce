from rest_framework import serializers
from .models import Payment
from orders.serializers import OrderSerializer
from orders.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.filter(payment_status=False),
        source='order',
        write_only=True
    )

    class Meta:
        model = Payment
        fields = [
            'id', 'order', 'order_id', 'amount', 'payment_method',
            'status', 'transaction_id', 'payment_details',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['amount', 'status', 'transaction_id', 'payment_details'] 