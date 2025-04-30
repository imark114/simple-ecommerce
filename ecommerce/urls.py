from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import admin_dashboard

schema_view = get_schema_view(
   openapi.Info(
      title="E-Commerce API",
      default_version='v1',
      description="API documentation for E-Commerce project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@ecommerce.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('api/', include('products.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('cart.urls')),
    
    # API Documentation URLs
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/docs/json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)