from django.contrib import admin

from .models import Order, OrderLine


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    empty_value_display = '---'
    list_display = ('get_name', 'get_price', 'get_weight', 'quantity')

    def get_name(self, obj):
        return obj.product.name

    def get_price(self, obj):
        return obj.product.price

    def get_weight(self, obj):
        return obj.product.weight


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ["product", "product_price", "product_weight", "quantity",]
    max_num = 0
    can_delete = False


    def product_price(self, obj):
        return obj.product.price

    def product_weight(self, obj):
        return obj.product.weight


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = '---'
    list_display = ('created', 'email', 'phone', 'get_user')
    inlines = (OrderLineInline,)

    def get_user(self, obj):
        return obj.user.username if obj.user else 'guest'
