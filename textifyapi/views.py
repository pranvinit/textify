from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import TextCreateForm
from .models import Text, User

class TextList(ListView):
    model = Text
    template_name = "textifyapi/textlist.html"

class TextCreate(CreateView):
    model = Text
    form_class = TextCreateForm
    template_name = "textifyapi/textcreate.html"


