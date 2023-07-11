from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, TemplateView
from apps.core.models import Product
from apps.order.models import OrderProduct
from apps.order.cart import Cart
from apps.order.forms import OrderForm


class CartTemplateView(TemplateView):
    template_name = 'order/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class AddCartView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        cart = Cart(request)
        cart.add(product)
        return redirect('order:cart')


class RemoveItemView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        cart = Cart(request)
        cart.remove_item(product)
        return redirect('order:cart')


class RemoveCartView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        cart = Cart(request)
        cart.remove(product)
        return redirect('order:cart')


class CheckoutTemplateView(TemplateView):
    template_name = 'order/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            address = request.POST.get('address')
            comment = request.POST.get('comment')
            form = OrderForm({
                'user': request.user,
                'name': request.user.name,
                'surname': request.user.surname,
                'phone': request.user.phone,
                'email': request.user.email,
                'address': address,
                'comment': comment,
            })
        else:
            form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            cart = Cart(request)
            for item in cart:
                OrderProduct.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity']
                )
            cart.clear()
        else:
            pass

        return redirect('core:index')
