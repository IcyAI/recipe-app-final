from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import recipe                #to access recipe model

# Create your views here.

def home(request):
   return render(request, 'recipes/home.html')

# Create your views here.
class RecipeListView(ListView):           #class-based view
   model = recipe                         #specify model
   template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(DetailView):                 #class-based view
   model = recipe                                 #specify model
   template_name = 'recipes/detail.html'          #specify template