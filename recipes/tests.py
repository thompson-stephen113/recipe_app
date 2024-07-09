from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipesSearchForm

class RecipeModelTest(TestCase):
    def setUpTestData():
        # Sets up non-modified objects used by all test methods
        Recipe.objects.create(
            name = "Tea",
            ingredients = "Tea Leaves, Sugar, Water",
            cooking_time = 5,
        )

    # ------------------------- Name ------------------------- 
    def test_recipe_name(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "name"
        field_label = recipe._meta.get_field("name").verbose_name

        # Compares value to expected result
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "name"
        max_length = recipe._meta.get_field("name").max_length

        # Compares value to expected result
        self.assertEqual(max_length, 50)

    # ------------------------- Ingredients ------------------------- #
    def test_ingredients_max_length(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "ingredients"
        max_length = recipe._meta.get_field("ingredients").max_length

        # Compares value to expected result
        self.assertEqual(max_length, 255)

    # ------------------------- Cooking Time ------------------------- #
    def test_cooking_time_value(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets the value of "cooking_time"
        cooking_time_value = recipe.cooking_time

        # Compares value to expected result
        self.assertIsInstance(cooking_time_value, int)

    # ------------------------- Difficulty ------------------------- #
    def test_difficulty_calulation(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Compares value to expected result
        self.assertEqual(recipe.difficulty, "Easy")

    # ------------------------- URL ------------------------- #
    def test_get_absolute_url(self):
        # Gets a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Compares value to expected result
        self.assertEqual(recipe.get_absolute_url(), "/collection/1")

class RecipeFormTest(TestCase):
    # ------------------------- Search ------------------------- #
    def test_search_form_valid_data(self):
        # Creates a RecipesSearchForm instance with valid data
        form = RecipesSearchForm(data={
            "search_by": "name",
            "search_term": "Test Recipe",
            "cooking_time": "",
            "difficulty": "",
        })

        # Checks if form is valid
        self.assertTrue(form.is_valid())

    def test_search_form_invalid_data(self):
        # Creates a RecipesSearchForm instance with empty data
        form = RecipesSearchForm(data={})

        # Checks if form is invalid
        self.assertFalse(form.is_valid())

    def test_search_form_field_labels(self):
        # Creates a RecipesSearchForm instance
        form = RecipesSearchForm()

        # Checks if "search_by" field label is "Search by"
        self.assertEqual(form.fields["search_by"].label, "Search by")

        # Checks if "search_term" field label is "Search term"
        self.assertEqual(form.fields["search_term"].label, "Search term")

        # Checks if "cooking_time" field label is "Cooking Time (minutes)"
        self.assertEqual(form.fields["cooking_time"].label, "Cooking Time (minutes)")

        # Checks if "difficulty" field label is "Difficulty"
        self.assertEqual(form.fields["difficulty"].label, "Difficulty")

class RecipeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creates test user
        cls.user = User.objects.create_user(username="testuser", password="12345")

        # Creates test recipes
        cls.recipe1 = Recipe.objects.create(name="Recipe 1", ingredients="ingredient1, ingredient2", cooking_time=10)
        cls.recipe2 = Recipe.objects.create(name="Recipe 2", ingredients="ingredient1, ingredient2", cooking_time=20)

    def setUp(self):
        # Initializes test client
        self.client = Client()

    def test_recipe_list_view_login_required(self):
        # Sends GET request to recipe list view
        response = self.client.get(reverse("recipes:list"))

        # Checks if response redirects to login page with the next parameter set to requested URL
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('recipes:list')}")

    def test_recipe_list_view(self):
        # Logs test user in
        self.client.login(username="testuser", password="12345")

        # Sends GET request to recipe list view
        response = self.client.get(reverse("recipes:list"))

        # Checks if response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Checks if correct template is used
        self.assertTemplateUsed(response, "recipes/collection.html")

        # Checks if response contains the first recipe name
        self.assertContains(response, "Recipe 1")

        # Checks if response contains the second recipe name
        self.assertContains(response, "Recipe 2")

    def test_recipe_detail_view_login_required(self):
        # Sends GET request to recipe detail view for the first recipe
        response = self.client.get(reverse("recipes:detail", kwargs={"pk": self.recipe1.pk}))

        # Checks if response redirects to login page with the next parameter set to requested URL
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('recipes:detail', kwargs={'pk': self.recipe1.pk})}")

    def test_recipe_detail_view(self):
        # Logs test user in
        self.client.login(username="testuser", password="12345")

        # Sends GET request to recipe detail view for the first recipe
        response = self.client.get(reverse("recipes:detail", kwargs={"pk": self.recipe1.pk}))

        # Checks if response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Checks if correct template is used
        self.assertTemplateUsed(response, "recipes/detail.html")

        # Checks if response contains the first recipe name
        self.assertContains(response, "Recipe 1")

    def test_search_view_login_required(self):
        # Sends GET request to search view
        response = self.client.get(reverse("recipes:search"))

        # Checks if response redirects to login page with the next parameter set to requested URL
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('recipes:search')}")

    def test_search_view(self):
        # Logs test user in
        self.client.login(username="testuser", password="12345")

        # Sends POST request to search view with valid data
        response = self.client.post(reverse("recipes:search"), data={
            "search_by": "name",
            "search_term": "Recipe 1",
            "cooking_time": "",
            "difficulty": "",
        })

        # Checks if response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Checks if correct template is used
        self.assertTemplateUsed(response, "recipes/search.html")

        # Checks if response contains the first recipe name
        self.assertContains(response, "Recipe 1")
