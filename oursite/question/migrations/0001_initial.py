# Generated by Django 2.2.5 on 2020-03-09 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.CharField(choices=[('Y', 'YES'), ('N', 'NO'), ('?', 'NOT SURE')], max_length=1)),
                ('test', models.CharField(max_length=2)),
            ],
        ),
    ]