from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Coupon)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    inlines = [ProductImageAdmin]


@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name']
    model = ColorVariant

@admin.register(StorageVariant)
class StorageVariantAdmin(admin.ModelAdmin):
    list_display = ['storage_num', 'price_extra']
    model = StorageVariant


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
