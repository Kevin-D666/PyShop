from django.contrib import admin
from .models import Product, Offers

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


admin.site.register(Product, ProductAdmin)


class ProductOffers(admin.ModelAdmin):
    list_display = ("code", "discount")


admin.site.register(Offers, ProductOffers)
