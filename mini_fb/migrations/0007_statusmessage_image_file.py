# Generated by Django 3.2.8 on 2021-11-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0006_alter_statusmessage_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]