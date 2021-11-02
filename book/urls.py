from django.urls import path
from . import views
from .views import RecipeDetailView

app_name = 'book'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search'), #search ingridients
    path('search_recipe/', views.SearchResultsView_recipe.as_view(), name='search_recipe'),#search recipe
    path('<int:pk>/', RecipeDetailView.as_view(), name='detail'),
]