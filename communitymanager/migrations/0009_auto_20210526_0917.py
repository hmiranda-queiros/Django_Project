# Generated by Django 2.1.15 on 2021-05-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0008_communaute_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='date_creation',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_creation',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
