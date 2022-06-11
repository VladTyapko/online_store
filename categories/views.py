from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Category, Product
from .filters import ProductFilter
from .import get_paginator_items

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def category_products(request, slug, pk):
    category = get_object_or_404(Category, slug=slug, pk=pk)
    products_category = category.products.all()
    products_filter = ProductFilter(request.GET, queryset=products_category)
    products = get_paginator_items(
        products_filter.qs, settings.PRODUCT_PAGINATE_BY, request.GET.get("page")
    )
    sort_by = request.GET.get("sort_by")

    return render(request, 'products.html', {'category': category,
                                             'products': products, 'sort_by': sort_by})


def product_add_to_checkout(request, slug, pk, product_pk):
    if 'cart' not in request.session:
        request.session['cart'] = list()
    request.session['cart'].append(int(product_pk))
    request.session.modified = True

    return redirect(reverse("categories:products", kwargs={'slug': slug, 'pk': pk}))


def checkout(request):
    if 'cart' not in request.session:
        return render(request, 'cart.html')

    cart = Product.objects.filter(pk__in=request.session['cart'])
    total_price = 0
    for line in request.session['cart']:
        product = Product.objects.get(pk=line)
        total_price += product.price
    return render(request, 'cart.html', {'products': cart, 'total_price': total_price})


def delete_product(request, pk):
    request.session['cart'] = list(filter((pk).__ne__, request.session['cart']))
    request.session.modified = True
    return redirect(reverse("categories:checkout"))