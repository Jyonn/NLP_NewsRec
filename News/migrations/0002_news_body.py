# Generated by Django 3.0.6 on 2022-03-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body',
            field=models.TextField(default=None),
        ),
    ]