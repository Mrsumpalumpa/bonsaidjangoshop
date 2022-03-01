from django import forms
from .models import contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'


class customusercreationform(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email','password1','password2']

    

