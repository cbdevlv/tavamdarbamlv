from django.contrib import admin
from .models import Product, Category, SizeType, Size, Color

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SizeType)
admin.site.register(Size)
admin.site.register(Color)
