from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'total_price')
    can_delete = False

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__email', 'user__username')
    readonly_fields = ('user', 'total_price', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'status', 'total_price')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'total_price')
    list_filter = ('order__status', 'created_at')
    search_fields = ('order__id', 'product__name')
    readonly_fields = ('order', 'product', 'quantity', 'price', 'total_price', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fieldsets = (
        ('Item Information', {
            'fields': ('order', 'product', 'quantity', 'price', 'total_price')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
