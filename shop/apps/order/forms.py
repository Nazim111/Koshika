from django import forms

from apps.order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['complete']


# robo_form = RobokassaForm(
#     initial={
#         'OutSum': order.amount,
#         'InvId': order.pk,
#         'Desc': order.description,
#         'UserIP': order.ip_address
#     },
#     login=conf.login,
#     password1=conf.password1,
#     password2=conf.password2
# )
