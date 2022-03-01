# Generated by Django 4.0.1 on 2022-02-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_alter_mcprofile_mc_profile_img'),
        ('grievance_data', '0004_alter_status_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='gri_priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='gri_severity',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='grievance',
            name='gri_upvote',
        ),
        migrations.AddField(
            model_name='grievance',
            name='gri_upvote',
            field=models.ManyToManyField(to='authapp.CitizenProfile'),
        ),
    ]
