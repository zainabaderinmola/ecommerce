# Generated by Django 3.1.5 on 2021-02-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
