# Generated by Django 3.2.9 on 2021-12-08 13:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('gn', 'General'), ('rm', 'Reminder'), ('th', 'Thought'), ('qt', 'Quote'), ('nt', 'Note')], max_length=2)),
                ('severity', models.CharField(choices=[('l', 'low'), ('m', 'moderate'), ('h', 'high')], max_length=1)),
                ('pinned', models.BooleanField(default=False)),
                ('images', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]