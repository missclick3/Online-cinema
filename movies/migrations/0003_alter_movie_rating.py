# Generated by Django 4.0.6 on 2022-07-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_options_movie_category_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(),
        ),
    ]