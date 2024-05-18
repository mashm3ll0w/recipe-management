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
      "title": TextInput(attrs={"class": "form-control listing-form", "placeholder": "Enter Recipe title"}),
      "description": Textarea(attrs={"class": "form-control listing-form", "cols": 20, "rows": 3, "placeholder": "Recipe description"}),
      "ingredients": Textarea(attrs={"class": "form-control listing-form", "cols": 20, "rows": 3, "placeholder": "Ingredients..."}),
      "cooking_instructions": Textarea(attrs={"class": "form-control listing-form", "cols": 20, "rows": 3, "placeholder": "How do you cook the meal?..."}),
      "difficulty_level": Select(attrs={"class": "form-control listing-form", "placeholder": "Select difficulty"})
    }
