# Generated by Django 5.0.1 on 2024-07-21 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_remove_donghonam_brand_remove_donghonam_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('1tr ĐẾN 2tr', '1tr ĐẾN 2tr'), ('1tr ĐẾN 2tr', '1tr ĐẾN 2tr'), ('2tr ĐẾN 3tr', '2tr ĐẾN 3tr'), ('3tr ĐẾN 4tr', '3tr ĐẾN 4tr'), ('4tr ĐẾN 5tr', '4tr ĐẾN 5tr')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='tag',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store_app.product'),
        ),
    ]