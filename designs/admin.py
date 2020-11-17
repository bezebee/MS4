from django.contrib import admin
from .models import Design, DesignCategory


class DesignAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'designcategory',
        'price',
        'image',
    )

    ordering = ('name',)


class DesignCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Design, DesignAdmin)
admin.site.register(DesignCategory, DesignCategoryAdmin)
