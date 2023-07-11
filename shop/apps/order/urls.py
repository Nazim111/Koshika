from django.urls import path
from apps.order.views import CartTemplateView, AddCartView, RemoveCartView, CheckoutTemplateView, RemoveItemView


app_name = 'order'

urlpatterns = [
    path('cart/', CartTemplateView.as_view(), name='cart'),
    path('add/<pk>/', AddCartView.as_view(), name='cart_add'),
    path('remove_item/<pk>/', RemoveItemView.as_view(), name='remove_item'),
    path('remove/<pk>', RemoveCartView.as_view(), name='cart_remove'),
    # path('clear/', ClearCartView.as_view(), name='cart_clear'),
    path('checkout/', CheckoutTemplateView.as_view(), name='checkout'),
]