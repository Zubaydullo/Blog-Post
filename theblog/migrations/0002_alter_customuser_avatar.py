# Generated by Django 4.0.1 on 2022-01-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='images/avatar.png', null=True, upload_to='images/users/%Y/%m'),
        ),
    ]