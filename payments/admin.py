from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('id', 'order', 'amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('id', 'order__id', 'transaction_id')
    readonly_fields = ('order', 'amount', 'payment_method', 'transaction_id', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fieldsets = (
        ('Payment Information', {
            'fields': ('order', 'amount', 'payment_method', 'status', 'transaction_id')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
