# Generated by Django 4.1.4 on 2022-12-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_movie_genre_alter_movie_budget_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(blank=True, to='main.genre'),
        ),
    ]
