# Generated by Django 4.1.5 on 2023-02-04 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrSystem', '0011_rename_description_job_job_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='description',
            new_name='service_name',
        ),
    ]
