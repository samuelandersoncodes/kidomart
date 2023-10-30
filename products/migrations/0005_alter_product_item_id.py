# Generated by Django 3.2.22 on 2023-10-30 00:03

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_id',
            field=models.CharField(default=products.models.generate_item_id, max_length=50, unique=True),
        ),
    ]
