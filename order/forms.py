from django import forms
from .models import Order, OrderLine


class CreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("email", "phone", "address", "method_payment")

        labels = {
            "email": "Пошта",
            "phone": "Телефон",
            "address": "Адреса доставки",
            "method_payment": "Спосіб оплати"
        }

    def save(self, **kwargs):
        user = kwargs.pop('user')
        cart = kwargs.pop('cart')
        instance = super(CreateForm, self).save(**kwargs)
        if user.is_authenticated:
            instance.user = user
        instance.save()

        unique_cart = set(cart)

        for line in unique_cart:
            OrderLine.objects.create(order=instance, product_id=line, quantity=cart.count(line))

        return instance