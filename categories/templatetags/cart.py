from django.template import Library

register = Library()


@register.simple_tag
def count_lines(request):
    if 'cart' not in request.session:
        return 0
    count = request.session['cart']
    return len(count)


@register.simple_tag
def count_product(request, pk):
    cart = request.session['cart']
    count = cart.count(pk)
    return count
