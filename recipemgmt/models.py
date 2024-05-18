from django.db import models

# Create your models here.
class Recipe(models.Model):
  """
  Create a new Recipe item and add it to the database
  """
  DIFFICULTY_CHOICES = [
    ("EASY", "BEGINNER"),
    ("MEDIUM", "INTERMEDIATE"),
    ("HARD", "EXPERT")
  ]

  title = models.CharField(max_length=255, null=False, db_index=True)
  description = models.CharField(max_length=255, null=False)
  ingredients = models.TextField(null=False)
  cooking_instructions = models.TextField(null=False)
  difficulty_level = models.CharField(choices=DIFFICULTY_CHOICES, max_length=50, null=False)


  def __str__(self) -> str:
    return self.title
