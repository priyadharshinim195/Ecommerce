from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="object-fit:cover;"/>', obj.image.url)
        return "No Image"
    thumbnail.short_description = 'Image'

    list_display = ('thumbnail', 'name', 'category', 'price', 'discount_price', 'stock', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
