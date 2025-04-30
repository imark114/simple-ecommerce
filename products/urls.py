from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductListView,
    ProductDetailView,
)

urlpatterns = [
    path('catalog/categories/', CategoryListView.as_view(), name='category-list'),
    path('catalog/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('catalog/products/', ProductListView.as_view(), name='product-list'),
    path('catalog/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
] 