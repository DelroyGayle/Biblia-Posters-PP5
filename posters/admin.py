from django.contrib import admin
from .models import Poster, Category

class PosterAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Poster, PosterAdmin)
admin.site.register(Category, CategoryAdmin)