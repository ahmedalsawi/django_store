# Generated by Django 3.0.8 on 2020-07-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lang',
            field=models.CharField(default='en', max_length=10),
        ),
    ]