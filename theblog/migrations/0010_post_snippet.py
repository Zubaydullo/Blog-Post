# Generated by Django 3.2.2 on 2021-08-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click a post above!', max_length=255),
        ),
    ]