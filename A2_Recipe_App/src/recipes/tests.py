from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    # Creates test data
    def setUpTestData():
        # Sets up non-modified objects used by all test methods
        Recipe.objects.create(
            name = "Tea",
            ingredients = "Tea Leaves, Sugar, Water",
            cooking_time = 5,
        )

    # ------------------------- Name ------------------------- #
    # Defines test for recipe name
    def test_recipe_name(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "name"
        field_label = recipe._meta.get_field("name").verbose_name

        # Compares value to expected result
        self.assertEqual(field_label, "name")

    # Defines test for recipe name length
    def test_recipe_name_max_length(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "name"
        max_length = recipe._meta.get_field("name").max_length

        # Compares value to expected result
        self.assertEqual(max_length, 50)

    # ------------------------- Ingredients ------------------------- #
    # Defines test for recipe ingredients
    def test_ingredients_max_length(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "ingredients"
        max_length = recipe._meta.get_field("ingredients").max_length

        # Compares value to expected result
        self.assertEqual(max_length, 255)

    # ------------------------- Cooking Time ------------------------- #
    # Defines test for recipe cooking time
    def test_cooking_time_value(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets the value of "cooking_time"
        cooking_time_value = recipe.cooking_time

        # Compares value to expected result
        self.assertIsInstance(cooking_time_value, int)

    # ------------------------- Difficulty ------------------------- #
    # Defines test for recipe difficulty calculation
    def test_difficulty_calulation(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Compares value to expected result
        self.assertEqual(recipe.difficulty, "Easy")
