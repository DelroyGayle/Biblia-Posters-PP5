from django.contrib import admin

from .models import SpecialDays


class SpecialDaysAdmin(admin.ModelAdmin):

    model = SpecialDays

    list_display = ('special_days_firstday',
                    'special_days_lastday',
                    'special_days_id',)

    ordering = ('special_days_firstday',)


admin.site.register(SpecialDays, SpecialDaysAdmin)
