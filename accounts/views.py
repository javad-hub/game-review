from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
# Create your views here.

#def SignUpView(request):
#	return render(request, 'registration/signup.html',{})
#	success_url = reverse_lazy('login')

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
