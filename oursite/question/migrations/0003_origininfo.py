# Generated by Django 2.2.5 on 2020-03-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20200309_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
                ('airport', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
