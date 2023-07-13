from django.contrib import admin
from .models.assurances_models import Assurance
from .models.banks_models import Bank
from .models.countries_models import Country
from .models.departements_models import Departement
from .models.employees_models import Employee
from .models.jobs_models import Job
from .models.locations_models import Location
from .models.mouvements_models import Mouvement
from .models.regions_models import Region
from .models.services_models import Service
from .models.statuses_models import Status
from .models.withdrawals_models import Withdrawal

# Register your models here.
@admin.register(Assurance)
class AssuranceAdmin(admin.ModelAdmin):
    # Fields to use for add/edit/show page
    fields = ('assurance_type','description')
    # fields to display in search page
    list_display = ('assurance_type','description')
    # fields that will be a link in search page
    list_display_links = ('assurance_type','description')
    # Ordering allowed in the search page
    ordering = ('assurance_type','description')
    # Search fields allowed in the search page
    search_fields = ('assurance_type','description')

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    fields = ('bank_code','routing_number_bank','description')
    list_display = ('bank_code','routing_number_bank','description')
    list_display_links = ('bank_code',)
    ordering = ('bank_code',)
    search_fields = ('bank_code',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('country_name','region_id')
    list_display = ('country_name','region_id')
    list_display_links = ('country_name',)
    ordering = ('country_name',)
    search_fields = ('country_name',)

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    fields = ('departement_name','location_id','manager_id')
    list_display = ('departement_name','location_id','manager_id')
    list_display_links = ('departement_name',)
    ordering = ('departement_name',)
    search_fields = ('departement_name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('employee_id','last_name','first_name','sex','email','cin','nif','phone1','phone2','birth_date','hire_date','manager_id','service_id','status_id','assurance_id','job_id','bank_id','bank_account','mode_paiement',)
    list_display =   ('employee_id','last_name','first_name','sex','email','cin','nif','phone1','phone2','birth_date','hire_date','manager_id','service_id','status_id','assurance_id','job_id','bank_id','bank_account','mode_paiement',)
    list_display_links = ('employee_id','cin','nif')
    ordering = ('employee_id',)
    search_fields = ('employee_id','last_name','first_name','nif','cin')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ('job_title','salary',)
    list_display =('job_title','salary',)
    list_display_links = ('job_title',)
    ordering = ('job_title',)
    search_fields = ('job_title',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('street_address','postal_code','city','state_province','country_id',)
    list_display = ('street_address','postal_code','city','state_province','country_id',)
    list_display_links = ('street_address','city',)
    ordering = ('postal_code',)
    search_fields = ('postal_code','city')

@admin.register(Mouvement)
class MouvementAdmin(admin.ModelAdmin):
    fields = ('mouvement_type','description')
    list_display = ('mouvement_type','description')
    list_display_links = ('mouvement_type',)
    ordering = ('mouvement_type',)
    search_fields = ('mouvement_type',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    fields = ('region_name',)
    list_display = ('region_name',)
    list_display_links = ('region_name',)
    ordering = ('region_name',)
    search_fields = ('region_name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('service_name','departement_id')
    list_display =  ('service_name','departement_id')
    list_display_links = ('service_name',)
    ordering = ('service_name',)
    search_fields = ('service_name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fields = ('status_type',)
    list_display = ('status_type',)
    list_display_links = ('status_type',)
    ordering = ('status_type',)
    search_fields = ('status_type',)

@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    fields = ('withdrawal_name','withdrawal_amount','description',)
    list_display = ('withdrawal_name','withdrawal_amount','description',)
    list_display_links = ('withdrawal_name',)
    ordering = ('withdrawal_name',)
    search_fields = ('withdrawal_name',)