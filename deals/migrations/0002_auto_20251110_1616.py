from django.db import migrations
from django.db import models

class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),  # replace with your latest migration
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
