from rest_framework import serializers
from django.utils.text import slugify

from order.models import Order, OrderLine
from categories.models import Product


class OrderLineModel(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ('product', 'quantity')


class OrderSerializerPost(serializers.ModelSerializer):
    items = OrderLineModel(many=True)

    class Meta:
        model = Order
        fields = ('items', 'email', 'phone', 'address', 'method_payment', 'order_status')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderLine.objects.create(order=order, **item_data)
        return order


class OrderLineSerializerGet(serializers.Serializer):
    order_id = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_description = serializers.SerializerMethodField()
    product_weight = serializers.SerializerMethodField()
    quantity = serializers.IntegerField()

    def get_order_id(self, obj):
        return (obj.order.pk)

    def get_product_name(self, obj):
        return (obj.product.name if obj.product else None)

    def get_product_description(self, obj):
        return (obj.product.description if obj.product else None)

    def get_product_weight(self, obj):
        return (obj.product.weight if obj.product else None)


class ProductSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'description', 'price', 'weight', 'available')

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = slugify(name)
        product = Product.objects.create(slug=slug, **validated_data)
        return product


class ProductSerializerGet(serializers.Serializer):
    category_name = serializers.SerializerMethodField()
    category_slug = serializers.SerializerMethodField()
    name = serializers.CharField()
    slug = serializers.CharField()
    image = serializers.CharField()
    description = serializers.CharField()
    price = serializers.SerializerMethodField()
    weight = serializers.IntegerField()

    def get_category_name(self, obj):
        return (obj.category.name)

    def get_category_slug(self, obj):
        return (obj.category.slug)

    def get_price(self, obj):
        return (obj.price)

    def get_product_weight(self, obj):
        return (obj.weight)
