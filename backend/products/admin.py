from django.contrib import admin
from .models import Category, Product, Review, ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ProductImage)
