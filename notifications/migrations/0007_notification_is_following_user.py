# Generated by Django 3.0.6 on 2020-07-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_notification_is_requested_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_following_user',
            field=models.BooleanField(default=False),
        ),
    ]
