from django.db import models

# CATEGORY MODEL
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.name


# CAROUSEL MODEL
class CarouselImage(models.Model):
    image = models.ImageField(upload_to="carousel/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Carousel {self.id}"


# PRODUCT MODEL
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    image = models.ImageField(upload_to="products/")

    is_top_deal = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name

