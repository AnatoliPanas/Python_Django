# Generated by Django 5.1.7 on 2025-04-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(choices=[('Fantasy', 'Fantasy'), ('Science', 'Science'), ('Cooking', 'Cooking'), ('Business', 'Business'), ('Psychology', 'Psychology'), ('History', 'History')], max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
