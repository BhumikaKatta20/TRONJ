# Generated by Django 2.2.3 on 2020-03-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tronj', '0025_auto_20200306_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='python',
            field=models.IntegerField(default=0),
        ),
    ]
