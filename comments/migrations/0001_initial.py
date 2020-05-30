# Generated by Django 3.0.6 on 2020-05-29 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_comments_xtd', '0006_auto_20181204_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyComment',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.XtdComment')),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ('submit_date',),
                'permissions': [('can_moderate', 'Can moderate comments')],
                'abstract': False,
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
    ]