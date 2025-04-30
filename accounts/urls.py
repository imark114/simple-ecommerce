from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView
 
urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='user-register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='user-login'),
    path('auth/refresh/', CustomTokenObtainPairView.as_view(), name='token-refresh'),
] 