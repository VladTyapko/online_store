from django.utils.translation import pgettext_lazy
from django_filters import OrderingFilter, FilterSet

from .models import Product

SUBSCRIPTION_SORT_BY_FIELDS = {
    "name": pgettext_lazy("Subscription list sorting option", "Назва"),
    "price": pgettext_lazy("Subscription  list sorting option", "Ціна"),
    "weight": pgettext_lazy("Subscription  list sorting option", "Вага"),
}


class ProductFilter(FilterSet):
    sort_by = OrderingFilter(
        label=pgettext_lazy("Subscription list filter label", "Сортувати за"),
        fields=SUBSCRIPTION_SORT_BY_FIELDS.keys(),
        field_labels=SUBSCRIPTION_SORT_BY_FIELDS,
    )

    class Meta:
        model = Product
        fields = []