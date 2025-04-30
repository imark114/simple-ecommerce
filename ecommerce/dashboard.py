from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from products.models import Product
from orders.models import Order
from payments.models import Payment
from accounts.models import CustomUser

def dashboard_callback(request, context):
    # Get today's date
    today = timezone.now().date()
    
    # Get last 7 days
    last_week = today - timedelta(days=7)
    
    # Get last 30 days
    last_month = today - timedelta(days=30)
    
    # Sales statistics
    today_sales = Order.objects.filter(created_at__date=today).aggregate(
        total_sales=Sum('total_price')
    )['total_sales'] or 0
    
    weekly_sales = Order.objects.filter(created_at__date__gte=last_week).aggregate(
        total_sales=Sum('total_price')
    )['total_sales'] or 0
    
    monthly_sales = Order.objects.filter(created_at__date__gte=last_month).aggregate(
        total_sales=Sum('total_price')
    )['total_sales'] or 0
    
    # Order statistics
    today_orders = Order.objects.filter(created_at__date=today).count()
    weekly_orders = Order.objects.filter(created_at__date__gte=last_week).count()
    monthly_orders = Order.objects.filter(created_at__date__gte=last_month).count()
    
    # Product statistics
    total_products = Product.objects.count()
    available_products = Product.objects.filter(available=True).count()
    low_stock_products = Product.objects.filter(stock__lt=10).count()
    
    # User statistics
    total_users = CustomUser.objects.count()
    new_users_today = CustomUser.objects.filter(date_joined__date=today).count()
    new_users_week = CustomUser.objects.filter(date_joined__date__gte=last_week).count()
    
    # Payment statistics
    successful_payments = Payment.objects.filter(status='completed').count()
    pending_payments = Payment.objects.filter(status='pending').count()
    failed_payments = Payment.objects.filter(status='failed').count()
    
    # Recent orders
    recent_orders = Order.objects.select_related('user').order_by('-created_at')[:10]
    
    # Add statistics to context
    context.update({
        'today_sales': today_sales,
        'weekly_sales': weekly_sales,
        'monthly_sales': monthly_sales,
        'today_orders': today_orders,
        'weekly_orders': weekly_orders,
        'monthly_orders': monthly_orders,
        'total_products': total_products,
        'available_products': available_products,
        'low_stock_products': low_stock_products,
        'total_users': total_users,
        'new_users_today': new_users_today,
        'new_users_week': new_users_week,
        'successful_payments': successful_payments,
        'pending_payments': pending_payments,
        'failed_payments': failed_payments,
        'recent_orders': recent_orders,
    })
    
    return context 