# Generated by Django 4.1 on 2022-09-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='review',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='watched',
            field=models.TextField(default=''),
        ),
    ]