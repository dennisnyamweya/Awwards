# Generated by Django 2.2.5 on 2019-09-09 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190909_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='manager',
            new_name='user',
        ),
    ]
