# Generated by Django 4.1.5 on 2023-02-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrSystem', '0013_employee_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.CharField(choices=[('MASCULINE', 'MASCULINE'), ('FEMININE', 'FEMININE')], max_length=15),
        ),
    ]
