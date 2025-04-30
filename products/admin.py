from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'available', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'available')
    inlines = [ProductImageInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Basic Information', {
                'fields': ('name', 'slug', 'description', 'category')
            }),
            ('Pricing and Stock', {
                'fields': ('price', 'stock', 'available')
            }),
            ('Images', {
                'fields': ('image',)
            })
        ]
        if obj:  # Only show timestamps in change view, not add view
            fieldsets.append(
                ('Timestamps', {
                    'fields': ('created_at', 'updated_at'),
                    'classes': ('collapse',)
                })
            )
        return fieldsets

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
