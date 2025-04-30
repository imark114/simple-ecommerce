from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from .filters import ProductFilter
from rest_framework.permissions import AllowAny
# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'name']

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductDetailSerializer
