# Generated by Django 2.2 on 2021-06-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0016_auto_20210602_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lu',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
