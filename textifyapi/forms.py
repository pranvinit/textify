from django import forms
from .models import Text

class TextCreateForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'