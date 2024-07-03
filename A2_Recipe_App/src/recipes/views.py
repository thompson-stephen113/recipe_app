from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
# FBV "home"
def home(request):
    return render(request, "recipes/recipes_home.html")

# CBV "RecipeList"
class RecipeListView(ListView):
    model = Recipe

    template_name = "recipes/collection.html"

# CBV "RecipeDetail"
class RecipeDetailView(DetailView):
    model = Recipe

    template_name = "recipes/detail.html"
