from django.contrib import admin
from the_foodhub.menu.models import Category, FoodItem


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem)