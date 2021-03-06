from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from textifyapi.forms import UserLoginForm

urlpatterns = [
    path('', views.textlist, name="textlist"),
    path('search/', views.search, name="search"),
    path('text/<pk>', views.TextDetailView.as_view(), name="textdetail" ),
    path('textdelete/<pk>', views.TextDelete.as_view(), name="textdelete"),
    path('textupdate/<pk>', views.TextUpdate.as_view(), name="textupdate"),
    path('create/', views.TextCreate.as_view(), name="textcreate"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form = UserLoginForm), name="login"),
    path('logoutview/', views.userlogout, name="logoutview"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('pin/<pk>', views.pintext, name="pintext"),
    path('unpin/<pk>', views.unpintext, name="unpintext"),
    path('setseverity/<slug:severity>/<int:pk>', views.setseverity, name="setseverity"),
    path('profile/<pk>', views.ProfileView.as_view(), name="profiledetail"),
    path('profileupdate/<pk>', views.ProfileUpdate.as_view(), name="profileupdate"),
    path('profiledelete/<pk>', views.ProfileDelete.as_view(), name="profiledelete")
]