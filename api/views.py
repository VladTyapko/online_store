from rest_framework.response import Response
from rest_framework.views import APIView

from order import OrderStatus
from order.models import OrderLine

from categories.models import Product

from .serializers import (
    OrderLineSerializerGet,
    OrderSerializerPost,
    ProductSerializerGet,
    ProductSerializerPost)


class ApiOrdersView(APIView):
    def get(self, request):
        orders = OrderLine.objects.filter(order__order_status=OrderStatus.IN_PROCESS)
        serializer = OrderLineSerializerGet(orders, many=True)
        return Response({"success": 'true', "orders": serializer.data})

    def post(self, request):
        order = request.data
        serializer = OrderSerializerPost(data=order, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
            return Response({"success": "true", "id": order_saved.id})
        return Response({"success": "false"})

    # {
    #     "email": "test-post@gmail.com",
    #     "phone": "1213345",
    #     "address": "aasdddsa",
    #     "method_payment": "онлайн",
    #     "order_status": "готується",
    #     "items": [
    #         {"product": 6, "quantity": 2},
    #         {"product": 6, "quantity": 1}
    #     ]
    # }


class ApiProductsView(APIView):
    def get(self, request):
        products = Product.objects.filter(available=True)
        serializer = ProductSerializerGet(products, many=True)
        return Response({"success": 'true', "products": serializer.data})

    def post(self, request):
        product = request.data
        serializer = ProductSerializerPost(data=product, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
            return Response({"success": "true", "id": product_saved.id})
        return Response({"success": "false"})

    # {
    #     "category": 3,
    #     "name": "test",
    #     "description": "камамбер, радомер, маасдамер, моцарела",
    #     "price": 345,
    #     "weight": 140
    # }

