# Generated by Django 4.0.1 on 2022-02-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_alter_mcprofile_mc_profile_img'),
        ('grievance_data', '0005_alter_grievance_gri_priority_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='gri_upvote_list',
            field=models.ManyToManyField(to='authapp.CitizenProfile'),
        ),
        migrations.RemoveField(
            model_name='grievance',
            name='gri_upvote',
        ),
        migrations.AddField(
            model_name='grievance',
            name='gri_upvote',
            field=models.IntegerField(default=0),
        ),
    ]
