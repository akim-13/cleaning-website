# Generated by Django 5.0.7 on 2024-08-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_timestamp_comment_creation_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='timezone',
            field=models.CharField(default='Europe/Moscow', max_length=255),
        ),
    ]
