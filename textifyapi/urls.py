from django.urls import path
from . import views

urlpatterns = [
    path('', views.TextList.as_view(), name="textlist"),
    path('create/', views.TextCreate.as_view(), name="textcreate"),
]