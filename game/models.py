from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)


	def __str__(self):
		return self.name


class Game(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete= models.CASCADE,)
	company = models.CharField(max_length=200)
	image = models.ImageField(default='static/img/default.png')
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.name} | {self.category}"
