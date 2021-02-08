# Generated by Django 3.1.5 on 2021-02-08 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20210208_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderitem',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
    ]