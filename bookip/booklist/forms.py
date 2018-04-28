
from django.contrib.auth.models import User
from django import forms
from .models import books


class user_register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password']



class user_login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','password']






class add_book(forms.ModelForm):
    
    class Meta:
        model = books
        fields = ['name','author', 'genre','rating','stock','book_cover']
