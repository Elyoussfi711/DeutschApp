# Generated by Django 4.0 on 2022-01-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_post_post_language_alter_post_post_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_verified',
            field=models.BooleanField(default=False),
        ),
    ]