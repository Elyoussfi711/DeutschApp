# Generated by Django 4.0 on 2022-01-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_resource_alter_profile_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(choices=[('History', 'H'), ('Technology', 'T'), ('Science', 'S'), ('Novel', 'N'), ('Article', 'A'), ('General', 'G')], max_length=24),
        ),
    ]