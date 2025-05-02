from django.shortcuts import render
from rest_framework import generics, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from .filters import ProductFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can create categories'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().post(request, *args, **kwargs)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

    def put(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can update categories'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can update categories'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can delete categories'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().delete(request, *args, **kwargs)

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.all()

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can create products'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().post(request, *args, **kwargs)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.all()

    def put(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can update products'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can update products'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'detail': 'Only admin users can delete products'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().delete(request, *args, **kwargs)
