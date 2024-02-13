from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Review, ReviewAdmin)
