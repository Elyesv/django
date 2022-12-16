from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ['image_url','name','stock','price']
    
admin.site.register(Product)