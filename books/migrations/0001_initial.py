# Generated by Django 5.2 on 2025-04-13 20:53

import books.models.user
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_site', models.URLField(max_length=250)),
                ('biography', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'author_bio',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=45, unique=True)),
                ('email', models.EmailField(max_length=75, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('role', models.CharField(choices=[('ADMIN', 'ADMIN'), ('MODERATOR', 'MODERATOR'), ('LIB MEMBER', 'LIB MEMBER')], default='LIB MEMBER', max_length=35)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('bio', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author', to='books.authorbio')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('rating', models.FloatField(default=0.0)),
                ('genre', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Science', 'Science'), ('Cooking', 'Cooking'), ('Business', 'Business'), ('Psychology', 'Psychology'), ('History', 'History')], max_length=30)),
                ('release_year', models.DateField()),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=6)),
                ('discounted_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=6)),
                ('pages', models.SmallIntegerField(blank=True, null=True)),
                ('language', models.CharField(default='English', max_length=15)),
                ('isbn', models.CharField(max_length=50)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author')),
                ('publisher', models.ForeignKey(default=books.models.user.get_first_admin, on_delete=django.db.models.deletion.PROTECT, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
                'ordering': ('release_year',),
                'unique_together': {('title', 'author')},
            },
        ),
    ]
