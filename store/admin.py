from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'price', 'in_stock', 'created', 'updated', 'is_active']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock', 'is_active', ]
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
