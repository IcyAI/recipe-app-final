from django.test import TestCase
from .models import recipe

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