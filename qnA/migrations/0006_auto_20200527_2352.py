# Generated by Django 3.0.6 on 2020-05-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnA', '0005_auto_20200527_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(blank=True, to='qnA.Topic'),
        ),
    ]
