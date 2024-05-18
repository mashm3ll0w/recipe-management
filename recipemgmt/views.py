from django.shortcuts import render
from django.http import JsonResponse
from .models import Recipe

# Create your views here.

def list_recipes(request):
  recipes = Recipe.objects.all()
  return render(request, 'index.html', {
    "recipes": recipes
  })

def view_recipe(request, recipe_id):
  recipe = Recipe.objects.get(pk=recipe_id)
  return render(request, 'recipe.html', {
    "recipe": recipe
  })


def new_recipe(request):
  pass


def edit_recipe(request, recipe_id):
  pass


