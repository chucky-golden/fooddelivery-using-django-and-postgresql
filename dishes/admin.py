from django.contrib import admin

from . models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'price', 'chef')
    list_display_links = ('id', 'name')
    list_filter = ('chef',)
    list_editable = ('is_published',)
    search_fields = ('name', 'price')
    list_per_page = 25


admin.site.register(Dish, DishAdmin)
