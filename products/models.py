from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete all related images and their files
        for image in self.images.all():
            image.delete()
        # Delete main image file if exists
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', 'created_at']

    def __str__(self):
        return f"Image for {self.product.name}"

    def delete(self, *args, **kwargs):
        # Delete the image file from the filesystem
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

# Signal to delete ProductImage files on queryset/bulk delete
@receiver(post_delete, sender=ProductImage)
def delete_product_image_file(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
