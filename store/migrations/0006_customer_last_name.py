# Generated by Django 3.1.5 on 2021-02-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]