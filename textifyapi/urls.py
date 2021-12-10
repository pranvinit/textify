from django.urls import path
from . import views

urlpatterns = [
    path('', views.TextList.as_view(), name="textlist"),
    path('search/', views.search, name="search"),
    path('text/<pk>', views.TextDetailView.as_view(), name="textdetail" ),
    path('textdelete/<pk>', views.TextDelete.as_view(), name="textdelete"),
    path('textupdate/<pk>', views.TextUpdate.as_view(), name="textupdate"),
    path('create/', views.TextCreate.as_view(), name="textcreate"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]