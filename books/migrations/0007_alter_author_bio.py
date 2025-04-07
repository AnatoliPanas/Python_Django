# Generated by Django 5.2 on 2025-04-07 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_authorbio_author_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author', to='books.authorbio'),
        ),
    ]
