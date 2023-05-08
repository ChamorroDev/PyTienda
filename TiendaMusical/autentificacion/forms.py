from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class UserCreationCustom(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username','email','password','password2']
        ## todos los campos fields = '__all__'
