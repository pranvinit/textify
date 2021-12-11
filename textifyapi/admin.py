from django.contrib import admin
from .models import User, Text
from .forms  import UserForm
from django.contrib.auth.admin import UserAdmin

admin.site.register(Text)

class UserAdmin(UserAdmin):
    model = User
    add_form = UserForm
    
admin.site.register(User, UserAdmin)