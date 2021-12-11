from django import forms
from .models import Text

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('title', 'content', 'image', 'category', 'severity', 'pinned', 'user')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's on you mind?"}),       
            'image': forms.FileInput(attrs={'class': 'form-control'}),       
            'category': forms.Select(attrs={'class': 'form-control'}),       
            'severity': forms.Select(attrs={'class': 'form-control'}),           
            'user': forms.Select(attrs={'class': 'form-control'}),       
        }