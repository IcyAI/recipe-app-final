from django import forms  # import django forms
from .models import recipe

SEARCH_CHOICES = [
    ("name", "Recipe Name"),
    ("cookingTime", "Cooking Time in Minutes"),
    ("difficulty", "Difficulty"),
]


# define class-based Form imported from Django forms
class RecipesSearchForm(forms.Form):
    search_by = forms.ChoiceField(
        choices=SEARCH_CHOICES, required=True, label="Search by"
    )
    search_term = forms.CharField(max_length=100, required=False, label="Search term")
    cookingTime = forms.IntegerField(required=False, label="Cooking Time in Minutes")
    difficulty = forms.ChoiceField(
        choices=[
            ("Easy", "Easy"),
            ("Medium", "Medium"),
            ("Intermediate", "Intermediate"),
            ("Hard", "Hard"),
        ],
        required=False,
        label="Difficulty",
    )