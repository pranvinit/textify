from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class User(AbstractUser):
    GENDER_CHOICE = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    ]
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], null=True, blank=True)
    gender = models.CharField(max_length=1 ,choices=GENDER_CHOICE, null=True, blank=True)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="php/")

    def __str__(self):
        return self.username

class Text(models.Model):
    TEXT_CATEGORY = [
        ("gn", "General"),
        ("rm", "Reminder"),
        ("th", "Thought"),
        ("qt", "Quote"),
        ("nt", "Note")
    ]
    TEXT_SEVERITY = [
        ("l", "low"),
        ("m", "moderate"),
        ("h", "high")
    ]
    title = models.CharField(max_length=100, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.CharField(max_length=2, choices=TEXT_CATEGORY, default="gn")
    severity = models.CharField(max_length=1, choices=TEXT_SEVERITY, null=True, blank=True, default=None)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("textlist")
    
    class Meta:
        ordering = ["-created_at"]
