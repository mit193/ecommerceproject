# Generated by Django 3.0 on 2021-06-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_transaction_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='cart',
            field=models.CharField(default='', max_length=100),
        ),
    ]
