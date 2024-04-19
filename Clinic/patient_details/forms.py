from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import User_info ,Treatment
from django import forms

class login_form(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    
class add_form(ModelForm):
    class Meta:
        model=User_info
        fields='__all__'
    
class add_history(ModelForm):
    class Meta:
        model=Treatment
        fields='__all__'