from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(allow_unicode=True, default='')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('core:category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=0)
    discount_price = models.DecimalField(verbose_name='Цена (Скидка)', max_digits=5, decimal_places=0, null=True, blank=True)

    in_stock = models.BooleanField(verbose_name="В наличии", default=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')

    image_1 = models.ImageField(verbose_name='Изображение-1', blank=True, null=True, upload_to='product')
    image_2 = models.ImageField(verbose_name='Изображение-2', blank=True, null=True, upload_to='product')
    image_3 = models.ImageField(verbose_name='Изображение-3', blank=True, null=True, upload_to='product')
    image_4 = models.ImageField(verbose_name='Изображение-4', blank=True, null=True, upload_to='product')
    image_5 = models.ImageField(verbose_name='Изображение-5', blank=True, null=True, upload_to='product')

    count_views = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-pk', ]

    def get_absolute_url(self):
        return reverse('core:product_detail', kwargs={'slug_category': self.category.slug, 'pk': self.pk})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# class ProductImage(models.Model):
#     image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='product')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductCountViews(models.Model):
    sesId = models.CharField(max_length=150, db_index=True)
    productId = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.sesId)


class RequestCall(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказать звонок'
        verbose_name_plural = 'Заказать звонок'
