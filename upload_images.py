import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name='dgklj999k',
    api_key='959265639282665',
    api_secret='EUZhTd9WtX3KYFH8lRxZYtJ1ReM'
)

from products.models import Product

for product in Product.objects.all():
    if product.image:
        image_path = f"D:/App/ecommerce/media/{product.image}"
        if os.path.exists(image_path):
            result = cloudinary.uploader.upload(image_path)
            product.image = result['public_id']
            product.save()
            print(f"Uploaded: {product.name}")

print("Done!")