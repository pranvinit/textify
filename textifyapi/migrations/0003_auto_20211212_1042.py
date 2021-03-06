# Generated by Django 3.2.9 on 2021-12-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textifyapi', '0002_alter_text_severity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='category',
            field=models.CharField(choices=[('gn', 'General'), ('rm', 'Reminder'), ('th', 'Thought'), ('qt', 'Quote'), ('nt', 'Note')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='text',
            name='image',
            field=models.ImageField(blank=True, default='gn', null=True, upload_to='images/'),
        ),
    ]
