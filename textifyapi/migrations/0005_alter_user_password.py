# Generated by Django 3.2.9 on 2021-12-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textifyapi', '0004_auto_20211212_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
