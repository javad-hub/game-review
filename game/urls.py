from django.urls import path
from .views import HomePageView, DetailPageView, SearchView, CategoryView, Category_Only_View

urlpatterns = [
	path('', HomePageView, name="home"),
	path('categories/', Category_Only_View, name="category_only"),
	path('game/<int:pk>', DetailPageView.as_view(), name='detail'),
	path('serachview/',SearchView, name='search-view'),
	path('category/<str:cats>/', CategoryView, name='category'),
]