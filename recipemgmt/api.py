from ninja import NinjaAPI
from .models import Recipe
from .schema import RecipeSchema, RecipeCreateSchema, MessageSchema

api = NinjaAPI()

# Get all Recipes
@api.get("/recipes", response=list[RecipeSchema])
def recipes(request):
  return Recipe.objects.all()


# Get a single Recipe
@api.get("/recipes/{recipe_id}", response={200: RecipeSchema, 404:MessageSchema})
def recipe(request, recipe_id):
  try:
    recipe = Recipe.objects.get(pk=recipe_id)
    return 200, recipe
  except Recipe.DoesNotExist:
    return 404, {"message": "Recipe not found"}


# Create a new Recipe
@api.post("/recipes", response={201: RecipeSchema})
def create_recipe(request, recipe: RecipeCreateSchema):
  Recipe.objects.create(**recipe.dict())
  return recipe


# Delete a Recipe
@api.delete("/recipes/{recipe_id}", response={204: MessageSchema, 404: MessageSchema})
def delete_recipe(request, recipe_id):
  try:
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    return 204, {"message": "Recipe successfully deleted!"}
  except Recipe.DoesNotExist:
    return 404, {"message": "Recipe not found"}


# Edit a Recipe's details
@api.put("/recipes/{recipe_id}", response={200: RecipeSchema, 404: MessageSchema})
def update_recipe(request, recipe_id: int, data: RecipeCreateSchema):
  try:
    recipe = Recipe.objects.get(pk=recipe_id)
    for attribute, value in data.dict().items():
      setattr(recipe, attribute, value)
    recipe.save()
    return 200, recipe
  except Recipe.DoesNotExist:
    return 404, {"message": "Recipe not found"}
