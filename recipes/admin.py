from django.contrib import admin
from .models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "ingredients", "cooking_time", "display_difficulty")
    fields = ("name", "ingredients", "cooking_time", "pic")
    readonly_fields = ("display_difficulty",)

    def display_difficulty(self, obj):
        return obj.difficulty
    
    display_difficulty.short_description = "Difficulty"

admin.site.register(Recipe, RecipeAdmin)
