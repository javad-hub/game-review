from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Category, Game
# Create your views here.

choices = Category.objects.all().values_list('name','name')
category = Category.objects.all()
game = Game.objects.all()

choice_list = []

for item in choices:
	choice_list.append(item)

#class HomePageView(TemplateView):
#	model = Category, Game
#	template_name = 'index.html'

def HomePageView(request):
	return render(request, "index.html", {
		'choice_list':choice_list,
		'category':category,
		})


def Category_Only_View(request):
	return render(request, "categories_only.html", {
		'choice_list':choice_list,
		'category':category,
		'game':game,
		})


class DetailPageView(DetailView):
	model = Game
	template_name = 'detail.html'


def SearchView(request):
	if request.method == 'POST':
		searched = request.POST.get('searched', False)
		searchs = Game.objects.filter(name__contains = searched)
	return render(request, 'serach.html', {
		'searched':searched,
		'searchs':searchs,})


def CategoryView(request, cats):
	game_category = get_object_or_404(Category, name=cats)
	category_games = Game.objects.filter(category__name=cats)
	return render(request, 'categories.html', 
		{'cats':cats,
		'category_games':category_games,})