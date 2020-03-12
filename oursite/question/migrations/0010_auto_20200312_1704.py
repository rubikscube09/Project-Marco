# Generated by Django 2.1.7 on 2020-03-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_origininfo_num_travelers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.IntegerField(choices=[(0, 'Not at all'), (1, 'A little bit'), (2, 'Somewhat'), (3, 'Reasonably'), (4, 'Very much'), (5, 'Extremely')], max_length=1),
        ),
    ]