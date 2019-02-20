from django.contrib import admin

# Register your models here.
from searchdemo.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ) }


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)