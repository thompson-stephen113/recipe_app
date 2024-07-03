from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = "recipes"

urlpatterns = [
    path("", home),
    path("collection", RecipeListView.as_view(), name="list"),
    path("collection/<pk>", RecipeDetailView.as_view(), name="detail"),
]
