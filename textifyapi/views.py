from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Text, User

class TextList(ListView):
    model = Text
    template_name = "textifyapi/textlist.html"

