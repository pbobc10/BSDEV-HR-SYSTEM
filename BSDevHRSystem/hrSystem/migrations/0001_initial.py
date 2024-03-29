# Generated by Django 4.1.5 on 2023-01-29 04:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assurance_type', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_code', models.CharField(max_length=10, unique=True)),
                ('routing_number_bank', models.IntegerField(unique=True)),
                ('description', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement_id', models.IntegerField(unique=True)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1000.0)])),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1000.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mouvement_type', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrawal_name', models.CharField(max_length=10)),
                ('withdrawal_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_id', models.IntegerField(unique=True)),
                ('description', models.CharField(max_length=128, unique=True)),
                ('departement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='hrSystem.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=256)),
                ('postal_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=128)),
                ('state_province', models.CharField(max_length=128)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='hrSystem.country')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employe_id', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(100000000)])),
                ('last_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('cin', models.IntegerField()),
                ('nif', models.CharField(max_length=13)),
                ('phone1', models.CharField(max_length=9)),
                ('phone2', models.CharField(max_length=9)),
                ('birth_date', models.DateField()),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1000.0)])),
                ('bank_account', models.CharField(max_length=30)),
                ('mode_paiement', models.CharField(choices=[('EN FONCTION', 'EN FONCTION'), ('CESSE', 'CESSE')], max_length=11)),
                ('assurance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrSystem.assurance')),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrSystem.bank')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrSystem.job')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrSystem.employee')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrSystem.service')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrSystem.status')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.AddField(
            model_name='departement',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='hrSystem.location'),
        ),
        migrations.AddField(
            model_name='departement',
            name='manager_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='hrSystem.employee'),
        ),
        migrations.AddField(
            model_name='country',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='hrSystem.region'),
        ),
    ]
