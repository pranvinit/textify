from django import forms
from .models import Text, User
from django.contrib.auth.forms import UserCreationForm


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
    class Meta:
        model = User
        fields = ('name', 'age', 'gender', 'username', 'email', 'profile_pic')