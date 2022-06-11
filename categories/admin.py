from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '---'
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = '---'
    list_display = ('name', 'price', 'get_category')
    prepopulated_fields = {"slug": ("name",)}

    def get_category(self, obj):
        return obj.category.name
