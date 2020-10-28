from django.contrib import admin
from .models import Category, Character, Ingredient, Tea


@admin.register(Category, Character, Ingredient)
class OptionAdmin(admin.ModelAdmin):

    list_display = ("name",)


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
    )