from django.urls import path

from .views import *

urlpatterns = [
    path('orders/', ApiOrdersView.as_view()),
    path('products/', ApiProductsView.as_view()),
]