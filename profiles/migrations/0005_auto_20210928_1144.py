# Generated by Django 3.2.7 on 2021-09-28 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='profile',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]