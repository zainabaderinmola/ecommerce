# Generated by Django 3.1.5 on 2021-02-04 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='first_name',
        ),
    ]