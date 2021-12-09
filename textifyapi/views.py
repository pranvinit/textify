from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TextCreateForm
from .models import Text, User

class TextList(ListView):
    model = Text
    template_name = "textifyapi/textlist.html"

class TextCreate(CreateView):
    model = Text
    form_class = TextCreateForm
    template_name = "textifyapi/textcreate.html"

class TextUpdate(UpdateView):
    model = Text
    template_name = "textifyapi/textupdate.html"
    fields = "__all__"
    success_url = reverse_lazy("textlist")

class TextDelete(DeleteView):
    model = Text
    template_name = "textifyapi/textdelete.html"
    success_url = reverse_lazy("textlist")

class TextDetailView(DetailView):
    model = Text
    template_name = "textifyapi/textdetail.html"