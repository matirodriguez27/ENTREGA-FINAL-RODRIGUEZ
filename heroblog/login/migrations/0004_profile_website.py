# Generated by Django 4.0.4 on 2022-07-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(default='a@a.com'),
            preserve_default=False,
        ),
    ]