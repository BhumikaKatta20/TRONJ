# Generated by Django 2.2.3 on 2020-03-21 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tronj', '0035_auto_20200315_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_details',
            old_name='Job_timings_end',
            new_name='job_offered',
        ),
        migrations.RemoveField(
            model_name='company_details',
            name='Job_timings_start',
        ),
    ]
