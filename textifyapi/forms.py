from django import forms
from .models import Text, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('title', 'content', 'image', 'category', 'severity', 'pinned')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's on you mind?"}),       
            'image': forms.FileInput(attrs={'class': 'form-control'}),       
            'category': forms.Select(attrs={'class': 'form-control'}),       
            'severity': forms.Select(attrs={'class': 'form-control'}),           
        }
      

class UserForm(UserCreationForm):
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('name', 'age', 'gender', 'username', 'email', 'profile_pic')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),       
            'age': forms.TextInput(attrs={'class': 'form-control'}),       
            'gender': forms.Select(attrs={'class': 'form-control'}),       
            'username': forms.TextInput(attrs={'class': 'form-control'}),           
            'email': forms.EmailInput(attrs={'class': 'form-control'}),           
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),                   
        }
      
    

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))