from django.test import TestCase
from .models import recipe
from .forms import RecipesSearchForm

# Create your tests here.

class MyTestClass(TestCase):
      
    #create set up test
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        recipe.objects.create(name = 'tea', cookingTime = 5, ingredients = ['water', 'tea leaves', 'sugar'])

    #Test name field
    def test_recipe_name(self):
        # Get a recipe object to test
        test = recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = test._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')
    
    #Test name field length
    def test_recipe_name_max_length(self):
           # Get a recipe object to test
           test = recipe.objects.get(id=1)

           # Get the metadata for the 'name' field and use it to query its max_length
           max_length = test._meta.get_field('name').max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 20)

    #Test cooking_time field
    def test_recipe_cooking_time(self):
        # Get a recipe object to test
        test = recipe.objects.get(id=1)

        # Get the metadata for the 'cookingtime' field and use it to query its data
        field_label = test._meta.get_field('cookingTime').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'cookingTime')

    #Test ingredients field
    def test_recipe_ingredients(self):
        # Get a recipe object to test
        test = recipe.objects.get(id=1)

        # Get the metadata for the 'ingredients' field and use it to query its data
        field_label = test._meta.get_field('ingredients').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'ingredients')

    #Test ingredients field length
    def test_recipe_ingredients_max_length(self):
           # Get a recipe object to test
           test = recipe.objects.get(id=1)

           # Get the metadata for the 'ingredients' field and use it to query its max_length
           max_length = test._meta.get_field('ingredients').max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 255)
    
    def test_get_absolute_url(self):
       test = recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of recipe #1
       #and load the URL /books/list/1
       self.assertEqual(test.get_absolute_url(), '/list/1')



# SEARCH
class RecipeFormTest(TestCase):
    def test_search_form_valid_data(self):
        # create a RecipesSearchForm instance with valid data
        form = RecipesSearchForm(
            data={
                "search_by": "name",
                "search_term": "Test Recipe",
                "cookingTime": "",
                "difficulty": "",
            }
        )

        # check if form is valid
        self.assertTrue(form.is_valid())

    def test_search_form_invalid_data(self):
        # create a RecipesSearchForm instance with empty data
        form = RecipesSearchForm(data={})

        # check if form is invalid
        self.assertFalse(form.is_valid())

    def test_search_form_field_labels(self):
        # create a RecipesSearchForm instance
        form = RecipesSearchForm()

        # check if "search_by" field label is "Search by"
        self.assertEqual(form.fields["search_by"].label, "Search by")

        # check if "search_term" field label is "Search term"
        self.assertEqual(form.fields["search_term"].label, "Search term")

        # check if "cooking_time" field label is "Cooking Time (minutes)"
        self.assertEqual(form.fields["cookingTime"].label, "Cooking Time in Minutes")

        # check if "difficulty" field label is "Difficulty"
        self.assertEqual(form.fields["difficulty"].label, "Difficulty")