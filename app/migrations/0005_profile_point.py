# Generated by Django 3.1.3 on 2020-11-27 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_plantation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Point',
            field=models.IntegerField(default=0),
        ),
    ]