from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserChangeForm, UserCreationForm
# Register your models here.

class UserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User
	list_display = ['email','username','is_staff',]
	

admin.site.register(User, UserAdmin)