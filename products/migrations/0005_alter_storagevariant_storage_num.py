# Generated by Django 4.2.2 on 2023-07-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_storagevariant_remove_product_size_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagevariant',
            name='storage_num',
            field=models.CharField(max_length=100),
        ),
    ]
