from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Game
# Create your views here.

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

#class HomePageView(TemplateView):
#	model = Category, Game
#	template_name = 'index.html'

def HomePageView(request):
	return render(request, "index.html", {
		'choice_list':choice_list,
		})