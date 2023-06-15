# Generated by Django 4.0 on 2022-01-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_post_post_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_state',
            field=models.CharField(choices=[('Yet to happen', 'Will Happen'), ('Happening today', 'Heppening'), ('Already happened', 'Happened')], default='Yet to happen', max_length=24),
        ),
        migrations.AddField(
            model_name='thread',
            name='thread_state',
            field=models.CharField(choices=[('Open', 'Not Answered'), ('Answered', 'Answered')], default='Open', max_length=8),
        ),
    ]
