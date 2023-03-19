from django.contrib import admin
from .models import Women, Category

class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "time_create", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
