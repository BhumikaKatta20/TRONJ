# Generated by Django 2.2.3 on 2020-03-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tronj', '0040_auto_20200322_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='about_the_company',
            field=models.CharField(default=' ', max_length=120),
        ),
    ]
