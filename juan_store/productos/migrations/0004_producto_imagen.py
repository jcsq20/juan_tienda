# Generated by Django 3.0.5 on 2020-04-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='', upload_to='productos/'),
            preserve_default=False,
        ),
    ]