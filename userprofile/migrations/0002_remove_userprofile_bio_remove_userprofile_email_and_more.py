# Generated by Django 4.2.2 on 2023-06-28 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
