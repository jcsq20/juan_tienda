# Generated by Django 3.0.5 on 2020-05-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
