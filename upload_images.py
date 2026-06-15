import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

import cloudinary
import cloudinary.uploader
import time

cloudinary.config(
    cloud_name='dgklj999k',
    api_key='959265639282665',
    api_secret='EUZhTd9WtX3KYFH8lRxZYtJ1ReM'
)

from products.models import Product

count = 0
for product in Product.objects.all():
    if product.image:
        image_name = str(product.image)
        # Already uploaded to cloudinary — skip
        if 'res.cloudinary.com' in image_name or not image_name.startswith('products/'):
            print(f"⏭️ Skipping: {product.name}")
            continue
        image_path = f"D:/App/ecommerce/media/{image_name}.jpg"
        if os.path.exists(image_path):
            try:
                result = cloudinary.uploader.upload(image_path)
                product.image = result['public_id']
                product.save()
                count += 1
                print(f"✅ Uploaded: {product.name}")
                time.sleep(1)  # avoid timeout
            except Exception as e:
                print(f"❌ Error: {product.name} → {e}")
        else:
            print(f"❌ Not found: {image_path}")

print(f"Total uploaded: {count}")