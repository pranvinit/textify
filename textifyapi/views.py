from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TextCreateForm
from .models import Text, User


def search(request):
    if request.method == "POST":
        query = request.POST["searchQuery"]
        results = Text.objects.filter(title__contains=query)
        return render(request, "textifyapi/searchresults.html", { 'query': query ,'results': results})
    else:
        return render(request, "textifyapi/searchresults.html", {})

def pintext(request, pk):
    text = Text.objects.get(pk=pk)
    text.pinned = True
    text.save()
    return redirect(reverse_lazy("textlist"))

def unpintext(request, pk):
    text = Text.objects.get(pk=pk)
    text.pinned = False
    text.save()
    return redirect(reverse_lazy("textlist"))

def setseverity(request, severity, pk):
    text = Text.objects.get(pk=pk)
    if severity is not 'none':
        text.severity = severity
    else:
        text.severity = None
    text.save()
    return redirect(reverse_lazy("textlist"))

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

class SignUp(CreateView):
    model = User
    template_name = "registration/signup.html"
    fields = "__all__"
    success_url = reverse_lazy("textlist")



