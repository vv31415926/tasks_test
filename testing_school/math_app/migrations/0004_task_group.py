# Generated by Django 3.2.9 on 2021-12-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0003_auto_20211201_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='group',
            field=models.IntegerField(default=0),
        ),
    ]
