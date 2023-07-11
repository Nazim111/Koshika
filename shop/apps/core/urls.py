from django.contrib import admin
from django.urls import path
from .views import IndexView, catalog, product_detail, about_us, request_call, category_detail

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('about/', about_us, name='about'),
    # path('categories/', catalog, name='catalog'),
    path('catalog/', catalog, name='catalog'),
    path('categories/<slug>/', category_detail, name='category_detail'),
    path('products/<slug_category>/<pk>/', product_detail, name='product_detail'),
    path('request_call/', request_call, name='request_call'),
]
