# Generated by Django 3.1.5 on 2021-02-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20210208_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='orderitem',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='orderitem',
            field=models.ManyToManyField(to='store.OrderItem'),
        ),
    ]
