from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import Avg
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    brand = models.CharField(max_length=100, blank=True, null=True)   # 👈 ADD THIS
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = CloudinaryField('image', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.product.name} - {self.user.username}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_discount_percentage(self):
        if self.discount_price and self.price and self.discount_price < self.price:
            return int((1 - (self.discount_price / self.price)) * 100)
        return 0

    def __str__(self):
        return self.name




def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)


    def get_discount_percentage(self):
        if self.discount_price and self.price and self.discount_price < self.price:
            return int((1 - (self.discount_price / self.price)) * 100)
        return 0

    def __str__(self):
        return self.name
class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1–5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}★)"



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # prevents duplicate wishlist

    def __str__(self):
 
       return f"{self.user.username} - {self.product.name}"





