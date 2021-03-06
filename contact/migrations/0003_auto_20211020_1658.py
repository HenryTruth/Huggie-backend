# Generated by Django 3.2.7 on 2021-10-20 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20211014_1157'),
        ('contact', '0002_rename_contact_id_contact_sender_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_user',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_notification', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_notification', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_response',
            field=models.CharField(default='#d7880d', max_length=50),
        ),
    ]
