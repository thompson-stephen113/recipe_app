from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

# Create your views here.
# FBV "home"
def home(request):
    return render(request, "recipes/recipes_home.html")

# CBV "RecipeList", protected
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    template_name = "recipes/collection.html"

# CBV "RecipeDetail", protected
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe

    template_name = "recipes/detail.html"
