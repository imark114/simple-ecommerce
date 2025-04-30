from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import CustomUser, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    inlines = (UserProfileInline,)
    fieldsets = (
        ('Personal Information', {
            'fields': ('username', 'email', 'password', 'first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'created_at')
    search_fields = ('user__email', 'user__username', 'phone_number', 'address')
    readonly_fields = ('user', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fieldsets = (
        ('Profile Information', {
            'fields': ('user', 'phone_number', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
