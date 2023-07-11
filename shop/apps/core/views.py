from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import RequestCallModelForm
from .models import Category, Product, ProductCountViews
from django.views.generic import View

from ..order import cart


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        category_qs = Category.objects.all()
        b1 = Category.objects.get(title='Браслеты')
        s1 = Category.objects.get(title='Серьги')
        k1 = Category.objects.get(title='Колье')
        category_s = Product.objects.filter(category='1')[:4]
        category_xs = Product.objects.filter(category='1')[:2]
        product_qs = Product.objects.all().order_by('title')[:4]

        context['category_list'] = category_qs
        context['product_list'] = product_qs
        context['category_s'] = category_s
        context['category_xs'] = category_xs
        context['b1'] = b1
        context['s1'] = s1
        context['k1'] = k1
        return render(request, 'core/index.html', context)


def about_us(request):
    context = {}
    category_qs = Category.objects.all()
    category_lb = Product.objects.filter(category='1')[:3]
    category_lb_1 = Product.objects.filter(category='1')[3:5]
    category_lb_2 = Product.objects.filter(category='1')[:3]

    context['category_list'] = category_qs
    context['category_lb'] = category_lb
    context['category_lb_1'] = category_lb_1
    context['category_lb_2'] = category_lb_2
    return render(request, 'core/lookbook.html', context)


def catalog(request):
    context = {}
    category_qs = Category.objects.all()
    category_products_qs = Product.objects.filter(category='1')
    category_products_qs_1 = Product.objects.filter(category='2')

    products = []

    for i in range(0, len(category_products_qs), 5):
        products.append(category_products_qs[i:i + 3])
        products.append(category_products_qs[i + 3:i + 5])

    products_1 = []

    for i in range(0, len(category_products_qs), 5):
        products_1.append(category_products_qs_1[i:i + 3])
        products_1.append(category_products_qs_1[i + 3:i + 5])

    order_price = request.GET.get('order', 'price')
    order_pop = request.GET.get('order', 'count_views')

    context['products'] = products
    context['products_1'] = products_1
    context['category_list'] = category_qs
    context['category_products_qs'] = category_products_qs
    context['category_products_qs_1'] = category_products_qs_1
    context['category_products_qs'] = category_products_qs.order_by(order_price)
    context['category_products_qs'] = category_products_qs.order_by(order_pop)
    return render(request, 'core/catalog-1.html', context)


# def catalog(request):
#     context = {}
#     category_qs = Category.objects.all()
#     product_qs = Product.objects.all()
#     products = []
#
#     for i in range(0, len(product_qs), 5):
#         products.append(product_qs[i:i + 3])
#         products.append(product_qs[i + 3:i + 5])
#
#     context['products'] = products
#     context['category_list'] = category_qs
#
#     return render(request, 'core/catalog.html', context)


def category_detail(request, slug):
    context = {}
    category_qs = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)

    order_price = request.GET.get('order', 'price')
    order_pop = request.GET.get('order', 'count_views')
    category_products_qs = Product.objects.filter(category=category)

    context['category'] = category
    context['category_list'] = category_qs

    context['category_products_qs'] = category_products_qs.order_by(order_price)
    context['category_products_qs'] = category_products_qs.order_by(order_pop)
    return render(request, 'core/category_detail.html', context)


def product_detail(request, slug_category, pk):
    context = {}
    product = Product.objects.filter(pk=pk).first()
    category = get_object_or_404(Category, slug=slug_category)
    product_r = Product.objects.filter(category=category)[:3]
    product_r_1 = Product.objects.filter(category=category)[:2]
    product_r_2 = Product.objects.filter(category=category)[:1]

    img_list = []
    img_list.append(product.image_1)
    if product.image_2 is not None:
        img_list.append(product.image_2)
    if product.image_3 is not None:
        img_list.append(product.image_3)
    if product.image_4 is not None:
        img_list.append(product.image_4)
    if product.image_5 is not None:
        img_list.append(product.image_5)

    q = 1
    while q < 5:
        for i in img_list:
            if str(i) == '':
                img_list.remove(i)
        q += 1
        print(img_list)

    context['images'] = img_list
    context['product'] = product
    context['category'] = category
    context['product_r'] = product_r
    context['product_r_1'] = product_r_1
    context['product_r_2'] = product_r_2

    return render(request, 'core/product.html', context)


def request_call(request):
    context = {}
    form = RequestCallModelForm()

    if request.method == 'POST':
        form = RequestCallModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'core/request_call.html', context)
