# Generated by Django 4.0 on 2022-01-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_selected',
            field=models.BooleanField(default=False),
        ),
    ]
