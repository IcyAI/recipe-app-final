from django.db import models

# Create your models here.


class recipe(models.Model):

    name = models.CharField(max_length=20)
    cookingTime = models.IntegerField()
    ingredients = models.CharField( max_length= 255, help_text="Enter the ingredients, separated by a comma")
    difficulty = None

    def __str__(self):
        return "Name: {}, Cooking time: {} minutes, Ingredients: {}, Difficulty: {}".format(
            self.name,
            self.cookingTime,
            self.ingredients,
            self.difficulty or 'Not set'
        )