from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import TextForm, UserForm
from .models import Text, User

def search(request):
    if request.method == "POST":
        query = request.POST["searchQuery"]
        results = Text.objects.filter( user_id = request.user.id ,title__contains=query)
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

def userlogout(request):
    return render(request, 'textifyapi/logout.html')

@login_required
def textlist(request):
    text_list = Text.objects.filter(user_id = request.user.id)
    return render(request, 'textifyapi/textlist.html', {'text_list': text_list})


class TextCreate(LoginRequiredMixin ,CreateView):
    model = Text
    form_class = TextForm
    template_name = "textifyapi/textcreate.html"

class TextUpdate(LoginRequiredMixin ,UpdateView):
    model = Text
    template_name = "textifyapi/textupdate.html"
    form_class = TextForm
    success_url = reverse_lazy("textlist")

class TextDelete(LoginRequiredMixin ,DeleteView):
    model = Text
    template_name = "textifyapi/textdelete.html"
    success_url = reverse_lazy("textlist")

class TextDetailView(LoginRequiredMixin ,DetailView):
    model = Text
    template_name = "textifyapi/textdetail.html"

class SignUp(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserForm
    success_url = reverse_lazy("textlist")



