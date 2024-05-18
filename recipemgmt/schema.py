from ninja import Schema


class MessageSchema(Schema):
  message: str


class RecipeSchema(Schema):
  id: int
  title: str
  description: str
  ingredients: str
  cooking_instructions: str
  difficulty_level: str


class RecipeCreateSchema(Schema):
  title: str
  description: str
  ingredients: str
  cooking_instructions: str
  difficulty_level: str
