from django import forms
from django.forms import Textarea, TextInput, Select
from .models import Recipe


class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    exclude = ["id"]
    labels = {
      "title": "",
      "description": "",
      "ingredients": "",
      "cooking_instructions": "",
      "difficulty_level": ""
    }
    widgets = {
      "title": TextInput(attrs={"class": "block text-sm font-medium leading-6 text-gray-900", "placeholder": "Enter Recipe title"}),
      "description": Textarea(attrs={"class": "block text-sm font-medium leading-6 text-gray-900", "cols": 20, "rows": 3, "placeholder": "Recipe description"}),
      "ingredients": Textarea(attrs={"class": "block text-sm font-medium leading-6 text-gray-900", "cols": 20, "rows": 3, "placeholder": "Ingredients..."}),
      "cooking_instructions": Textarea(attrs={"class": "block text-sm font-medium leading-6 text-gray-900", "cols": 20, "rows": 3, "placeholder": "How do you cook the meal?..."}),
      "difficulty_level": Select(attrs={"class": "block text-sm font-medium leading-6 text-gray-900", "placeholder": "Select difficulty"})
    }
