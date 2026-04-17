from django.db import models
from products.models import Product

class Deal(models.Model):
    title = models.CharField(max_length=200)
    deal_type = models.CharField(max_length=20, choices=[('flash','Flash Deal'),('limited','Limited Deal')], default='limited')
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    products = models.ManyToManyField(Product)  # ManyToManyField
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def deal_price(self):
        return self.discounted_price

    def discount_percentage(self):
        if self.original_price > 0:
            discount = ((self.original_price - self.discounted_price) / self.original_price) * 100
            return f"{discount:.1f}%"
        return "0%"

    def __str__(self):
        return self.title
