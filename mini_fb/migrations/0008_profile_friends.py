# Generated by Django 3.2.8 on 2021-11-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0007_statusmessage_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='_mini_fb_profile_friends_+', to='mini_fb.Profile'),
        ),
    ]
