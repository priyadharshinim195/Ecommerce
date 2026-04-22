import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.core import serializers
from products.models import Category, Product
from deals.models import Deal

data = (
    list(Category.objects.all()) + 
    list(Product.objects.all()) +
    list(Deal.objects.all())
)

with open('ecomdata.json', 'w', encoding='utf-8') as f:
    f.write(serializers.serialize('json', data, indent=2, ensure_ascii=False))

print(f"Exported {len(data)} objects!")