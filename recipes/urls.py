from django.urls import path
from .views import home, sort
from .views import RecipeListView
from .views import RecipeDetailView

app_name = 'recipes' 

urlpatterns = [
   path('', home, name= "home"),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('sort/', sort, name = "sort")
]
