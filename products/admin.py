from django.contrib import admin
from .models import *



class ProductImagesAdmin(admin.StackedInline):
    model= ProductImages

class ProductAdmin(admin.ModelAdmin):
    # model= Product
    inlines = [ProductImagesAdmin]
    list_display= ['name', 'price', 'category']

admin.site.register(Category)
admin.site.register(ColorVarient)
admin.site.register(SizeVarient)

# admin.site.register(ProductImages,ProductImagesAdmin)
admin.site.register(Product, ProductAdmin)


# ///cart 
class CartItemAdmin(admin.StackedInline):
    model= CartItem


class CartAdmin(admin.ModelAdmin):
   
    inlines = [CartItemAdmin]
    list_display= ['user']

admin.site.register(Cart, CartAdmin)

