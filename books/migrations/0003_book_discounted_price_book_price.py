# Generated by Django 5.2 on 2025-04-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_authorbio_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discounted_price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=6),
        ),
    ]
