from django.contrib import admin
from apps.core.models import Product, Category, ProductCountViews, RequestCall


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


# class ProductImageAdmin(admin.TabularInline):
#     model = ProductImage
#     extra = 1


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [

    ]



admin.site.register(Product, ProductAdmin)
admin.site.register(RequestCall)
# admin.site.register(ProductCountViews)

# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 0
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [ProductInline]
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'category', 'in_stock')
#     list_display_links = ('title', 'price', 'category')
#     list_editable = ('in_stock',)
