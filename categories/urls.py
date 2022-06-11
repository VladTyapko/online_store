from django.urls import path

from .views import *

urlpatterns = [
    path('', categories_list, name="home"),
    path('checkout', checkout, name="checkout"),
    path('categories/<slug:slug>/<int:pk>', category_products, name="products"),
    path('categories/<slug:slug>/<int:pk>/<int:product_pk>', product_add_to_checkout, name="add-to-checkout"),
    path('delete/<int:pk>', delete_product, name="delete-product"),
]