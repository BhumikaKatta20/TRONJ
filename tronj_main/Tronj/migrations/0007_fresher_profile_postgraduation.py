# Generated by Django 2.2.3 on 2020-01-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tronj', '0006_auto_20200103_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='fresher_profile',
            name='PostGraduation',
            field=models.IntegerField(default=0),
        ),
    ]
