# Generated by Django 3.0.8 on 2020-07-01 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lang',
        ),
    ]
