# Generated by Django 4.1.5 on 2023-01-29 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrSystem', '0002_alter_employee_mode_paiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='manager_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='hrSystem.employee'),
        ),
    ]