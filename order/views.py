from django.shortcuts import render, redirect

from .forms import CreateForm
from . import MethodPayment
from categories.models import Product

def create_order(request):
    if request.method == 'POST':
        create_form = CreateForm(request.POST)
        if create_form.is_valid():
            my_cart = request.session['cart']
            create_form.save(user=request.user, cart=my_cart, commit=False)
            del request.session['cart']
            request.session.modified = True
            payment = create_form.cleaned_data['method_payment']

            if payment == MethodPayment.ONLINE:
                total_amount = 0
                for item in my_cart:
                    product = Product.objects.get(pk=item)
                    total_amount += product.price
                from cloudipsp import Api, Checkout
                api = Api(merchant_id=1396424,
                          secret_key='test')
                checkout = Checkout(api=api)
                data = {
                    "currency": "UAH",
                    "amount": round(total_amount)*100
                }
                url = checkout.url(data).get('checkout_url')
                return redirect(url)
            return render(request, 'successful.html')
    create_form = CreateForm()
    return render(request, 'create_order.html', {'create_form': create_form})


