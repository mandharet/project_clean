# Generated by Django 4.0.1 on 2022-01-21 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_user_ismcuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='loc_town',
        ),
    ]
