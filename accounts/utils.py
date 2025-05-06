from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from datetime import timedelta
import jwt

def generate_email_verification_token(user):
    """Generate a JWT token for email verification"""
    expiry = timezone.now() + timedelta(hours=settings.EMAIL_VERIFICATION_TOKEN_EXPIRY)
    token = jwt.encode(
        {
            'user_id': user.id,
            'exp': expiry.timestamp()
        },
        settings.SECRET_KEY,
        algorithm='HS256'
    )
    return token

def send_verification_email(user):
    """Send email verification link to user"""
    token = generate_email_verification_token(user)
    verification_url = f"http://localhost:8000/api/accounts/verify-email/{token}"
    
    context = {
        'user': user,
        'verification_url': verification_url
    }
    
    html_message = render_to_string('accounts/email/verification_email.html', context)
    plain_message = strip_tags(html_message)
    
    send_mail(
        'Verify your email address',
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )

def send_order_status_email(user, order):
    """Send order status update email to user"""
    context = {
        'user': user,
        'order': order,
        'order_status': order.status
    }
    
    html_message = render_to_string('orders/email/order_status_update.html', context)
    plain_message = strip_tags(html_message)
    
    send_mail(
        f'Order Status Update - Order #{order.id}',
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    ) 