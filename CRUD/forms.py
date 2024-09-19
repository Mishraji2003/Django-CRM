from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    first_name = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    password1 = forms.PasswordInput(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Passowrd'}))
    password2 = forms.PasswordInput(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Passowrd again'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


