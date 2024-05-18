from django.urls import path
from .api import api
from . import views

urlpatterns = [
    path("", views.list_recipes, name="recipes"),
    path("recipes/<int:recipe_id>", views.view_recipe, name='view_recipe'),
    path("recipes/create", views.new_recipe, name="new_recipe"),
    path("recipes/edit/<int:recipe_id>", views.edit_recipe, name="edit_recipe"),

    # API routes
    path("api/", api.urls),
]
