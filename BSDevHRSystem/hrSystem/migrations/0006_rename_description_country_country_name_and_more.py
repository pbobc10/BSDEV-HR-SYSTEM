# Generated by Django 4.1.5 on 2023-02-01 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrSystem', '0005_assurance_description_alter_employee_cin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='description',
            new_name='country_name',
        ),
        migrations.RemoveField(
            model_name='departement',
            name='departement_id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Service_id',
        ),
    ]
