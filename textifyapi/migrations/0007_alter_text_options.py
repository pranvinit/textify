# Generated by Django 3.2.9 on 2021-12-09 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textifyapi', '0006_auto_20211209_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['-created_at']},
        ),
    ]
