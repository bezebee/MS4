from django.contrib import admin
from .models import Sketch, Sheet

# Register your models here.

class SketchAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'sheet',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class SheetAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Sketch, SketchAdmin)
admin.site.register(Sheet, SheetAdmin)
