from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'descripition')
    search_fields = ('product',)


admin.site.register(models.Inflow, InflowAdmin)
