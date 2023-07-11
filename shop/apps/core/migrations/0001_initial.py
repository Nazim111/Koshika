# Generated by Django 4.1.6 on 2023-03-10 12:07

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Цена')),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Фото +модель')),
                ('image_small', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Фото-товар')),
                ('image_add_1', models.ImageField(blank=True, null=True, upload_to='product')),
                ('image_add_2', models.ImageField(blank=True, null=True, upload_to='product')),
                ('image_add_3', models.ImageField(blank=True, null=True, upload_to='product')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
                ('count_views', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='core.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='RequestCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказать звонок',
                'verbose_name_plural': 'Заказать звонок',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCountViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sesId', models.CharField(db_index=True, max_length=150)),
                ('productId', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
