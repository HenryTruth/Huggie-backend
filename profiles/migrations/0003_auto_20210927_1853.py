# Generated by Django 3.2.7 on 2021-09-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210926_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='longtitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
