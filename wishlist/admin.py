from django.contrib import admin
from .models import Wishlist

# Register your models here.


class WishlistAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Wishlist, WishlistAdmin)
