from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
        ('products', '0003_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        # Empty - products field already added in 0001_initial
    ]