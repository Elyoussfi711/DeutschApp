# Generated by Django 4.0 on 2022-01-27 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_reply_reply_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='index.post'),
            preserve_default=False,
        ),
    ]