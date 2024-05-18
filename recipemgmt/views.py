from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Recipe
from django.urls import reverse
from .forms import RecipeForm

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
  if request.method == "POST":
    form = RecipeForm(request.POST)
    if form.is_valid:
      title = request.title
      description = request.description
      ingredients = request.ingredients
      cooking_instructions = request.cooking_instructions
      difficulty_level = request.difficulty_level
      new_recipe = Recipe(title=title, description=description, ingredients=ingredients, cooking_instructions=cooking_instructions, difficulty_level=difficulty_level)
      new_recipe.save()
      return HttpResponseRedirect(reverse('recipes'))
    else:
      return render(request, "new_recipe.html", {
        "form": RecipeForm(request.POST)
      })
  return render(request, "new_recipe.html", {
    "form": RecipeForm
  })


def edit_recipe(request, recipe_id):
  pass


