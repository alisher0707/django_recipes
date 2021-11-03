from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import generic
from .models import Recipe, Ingredient

class IndexView(generic.ListView):
    template_name = 'book/index.html'
    context_object_name = 'alpha_recipe_list'

    def get_queryset(self):
        """Return all recipes in alpha order."""
        return Recipe.objects.order_by('title')

def index(request):
    alpha_recipe_list = Recipe.objects.order_by('title')
    alpha_recipe_listt = Recipe.objects.order_by('title')
    context = {
        'alpha_recipe_list': alpha_recipe_list,
        'alpha_recipe_listt': alpha_recipe_listt,
    }
    return render(request, 'book/index.html', context) # returns an HttpR with rendered template and context

class SearchResultsView(ListView):
    model = Ingredient
    template_name = 'book/search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['ingredient_name'] = self.request.GET['ingredient_name']
        context['num_recipes'] = context['recipe_list'].count()
        return context
    
    def get_queryset(self):
        ingredient_name = self.request.GET['ingredient_name']
        recipe_list = Recipe.objects.filter(ingredients__name=ingredient_name).order_by('title')
        return recipe_list

class SearchResultsView_recipe(ListView):
    model = Recipe
    template_name = 'book/search_recipe.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView_recipe, self).get_context_data(**kwargs)
        context['recipe_name'] = self.request.GET['recipe_name']
        context['num_recipes'] = context['recipe_list'].count()
        return context

    def get_queryset(self):
        recipe_name = self.request.GET['recipe_name']
        recipe_list = Recipe.objects.filter(title=recipe_name).order_by('title')
        return recipe_list

def search(request):
    alpha_recipe_list = Recipe.objects.order_by('title')[:5]
    print("COUNT: ", + alpha_recipe_list.count())
    context = {
        'alpha_recipe_list': alpha_recipe_list,
        'num_ingredients': alpha_recipe_list.count(),
    }
    return render(request, 'book/search.html', context)

def search_recipe(request):
    alpha_recipe_listt = Recipe.objects.order_by('title')[:5]
    print("COUNT: ", + alpha_recipe_listt.count())
    context = {
        'alpha_recipe_listt': alpha_recipe_listt,
        'num_recipe': alpha_recipe_listt.count(),
    }

    return render(request, 'book/search_recipe.html', context)

class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        recipe = self.object
        ingredients_list = recipe.ingredients.through.objects.all().filter(recipe=recipe)
        steps = recipe.steps
        steps_listed = steps.split("+")
        context = {
            'recipe': recipe,
            'steps': steps_listed,
            'ingredients': ingredients_list,
        }
        return context