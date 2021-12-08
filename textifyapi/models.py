from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField


class User(models.Model):
    GENDER_CHOICE = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length=1 ,choices=GENDER_CHOICE)
    email = models.EmailField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

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
    category = models.CharField(max_length=2, choices=TEXT_CATEGORY)
    severity = models.CharField(max_length=1, choices=TEXT_SEVERITY)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_at"]
