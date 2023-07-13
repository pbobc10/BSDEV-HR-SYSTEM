"""BSDevHRSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from .views.assurances_view import AssuranceListView, AssuranceCreateView,AssuranceDetailView,AssuranceUpdateView,AssuranceDeleteView
from .views.banks_view import BankCreateView,BankDeleteView,BankDetailView,BankListView,BankUpdateView,csv
from .views.leaves_view import LeaveCreateView,LeaveDeleteView,LeaveDetailView,LeaveListView,LeaveUpdateView
from .views.country_view import CountryCreateView,CountryDeleteView,CountryDetailView,CountryListView,CountryUpdateView
from .views.departement_view import DepartementCreateView,DepartementDeleteView,DepartementDetailView,DepartementListView,DepartementUpdateView
from .views.employees_view import EmployeeCreateView,EmployeeDeleteView,EmployeeDetailView,EmployeeListView,EmployeeUpdateView
from .views.jobs_view import JobCreateView,JobDeleteView,JobDetailView,JobListView,JobUpdateView
from .views.locations_view import LocationCreateView,LocationDeleteView,LocationDetailView,LocationListView,LocationUpdateView
from .views.mouvements_view import MouvementCreateView,MouvementDeleteView,MouvementDetailView,MouvementListView,MouvementUpdateView
from .views.regions_view import RegionCreateView,RegionDeleteView,RegionDetailView,RegionListView,RegionUpdateView
from .views.services_view import ServiceCreateView,ServiceDeleteView,ServiceDetailView,ServiceListView,ServiceUpdateView
from .views.statuses_view import StatusCreateView,StatusDeleteView,StatusDetailView,StatusListView,StatusUpdateView
from .views.withdrawals_view import WithdrawalCreateView,WithdrawalDeleteView,WithdrawalDetailView,WithdrawalListView,WithdrawalUpdateView
from .views.dashboard_view import DashboardView

app_name = 'hrSystem'

urlpatterns=[
    #Dashboard
     re_path('^dashboard/$',DashboardView.as_view(),name='dashboard'),
    #Assurance
    re_path('^assurance/$',AssuranceListView.as_view(),name='assurance-list'),
    re_path('^assurance/(?P<pk>\d+)/$',AssuranceDetailView.as_view(),name='assurance-detail'),
    re_path('^assurance/create/$',AssuranceCreateView.as_view(),name='assurance-create'),
    re_path('^assurance/update/(?P<pk>\d+)/$',AssuranceUpdateView.as_view(),name='assurance-update'),
    re_path('^assurance/delete/(?P<pk>\d+)/$',AssuranceDeleteView.as_view(),name='assurance-delete'),
    # Banks
    re_path('^bank/$',BankListView.as_view(),name='bank-list'),
    re_path('^bank/(?P<pk>\d+)/$',BankDetailView.as_view(),name='bank-detail'),
    re_path('^bank/create/$',BankCreateView.as_view(),name='bank-create'),
    re_path('^bank/update/(?P<pk>\d+)/$',BankUpdateView.as_view(),name='bank-update'),
    re_path('^bank/delete/(?P<pk>\d+)/$',BankDeleteView.as_view(),name='bank-delete'),
    re_path('^bank/csv/$',csv,name='bank-csv'),
    # Leaves
    re_path('^leave/$',LeaveListView.as_view(),name='leave-list'),
    re_path('^leave/(?P<pk>\d+)/$',LeaveDetailView.as_view(),name='leave-detail'),
    re_path('^leave/create/$',LeaveCreateView.as_view(),name='leave-create'),
    re_path('^leave/update/(?P<pk>\d+)/$',LeaveUpdateView.as_view(),name='leave-update'),
    re_path('^leave/delete/(?P<pk>\d+)/$',LeaveDeleteView.as_view(),name='leave-delete'),
    #Country
    re_path('^country/$',CountryListView.as_view(),name='country-list'),
    re_path('^country/(?P<pk>\d+)/$',CountryDetailView.as_view(),name='country-detail'),
    re_path('^country/create/$',CountryCreateView.as_view(),name='country-create'),
    re_path('^country/update/(?P<pk>\d+)/$',CountryUpdateView.as_view(),name='country-update'),
    re_path('^country/delete/(?P<pk>\d+)/$',CountryDeleteView.as_view(),name='country-delete'),
    #Departement
    re_path('^departement/$',DepartementListView.as_view(),name='departement-list'),
    re_path('^departement/(?P<pk>\d+)/$',DepartementDetailView.as_view(),name='departement-detail'),
    re_path('^departement/create/$',DepartementCreateView.as_view(),name='departement-create'),
    re_path('^departement/update/(?P<pk>\d+)/$',DepartementUpdateView.as_view(),name='departement-update'),
    re_path('^departement/delete/(?P<pk>\d+)/$',DepartementDeleteView.as_view(),name='departement-delete'),
    #Employee
    re_path('^employee/$',EmployeeListView.as_view(),name='employee-list'),
    re_path('^employee/(?P<pk>\d+)/$',EmployeeDetailView.as_view(),name='employee-detail'),
    re_path('^employee/create/$',EmployeeCreateView.as_view(),name='employee-create'),
    re_path('^employee/update/(?P<pk>\d+)/$',EmployeeUpdateView.as_view(),name='employee-update'),
    re_path('^employee/delete/(?P<pk>\d+)/$',EmployeeDeleteView.as_view(),name='employee-delete'),
    re_path('^employee/detail/(?P<pk>\d+)/$',EmployeeDetailView.as_view(),name='employee-detail'),
    #Job
    re_path('^job/$',JobListView.as_view(),name='job-list'),
    re_path('^job/(?P<pk>\d+)/$',JobDetailView.as_view(),name='job-detail'),
    re_path('^job/create/$',JobCreateView.as_view(),name='job-create'),
    re_path('^job/update/(?P<pk>\d+)/$',JobUpdateView.as_view(),name='job-update'),
    re_path('^job/delete/(?P<pk>\d+)/$',JobDeleteView.as_view(),name='job-delete'),
    #Location
    re_path('^location/$',LocationListView.as_view(),name='location-list'),
    re_path('^location/(?P<pk>\d+)/$',LocationDetailView.as_view(),name='location-detail'),
    re_path('^location/create/$',LocationCreateView.as_view(),name='location-create'),
    re_path('^location/update/(?P<pk>\d+)/$',LocationUpdateView.as_view(),name='location-update'),
    re_path('^location/delete/(?P<pk>\d+)/$',LocationDeleteView.as_view(),name='location-delete'),
    #Mouvement
    re_path('^mouvement/$',MouvementListView.as_view(),name='mouvement-list'),
    re_path('^mouvement/(?P<pk>\d+)/$',MouvementDetailView.as_view(),name='mouvement-detail'),
    re_path('^mouvement/create/$',MouvementCreateView.as_view(),name='mouvement-create'),
    re_path('^mouvement/update/(?P<pk>\d+)/$',MouvementUpdateView.as_view(),name='mouvement-update'),
    re_path('^mouvement/delete/(?P<pk>\d+)/$',MouvementDeleteView.as_view(),name='mouvement-delete'),
    #Region
    re_path('^region/$',RegionListView.as_view(),name='region-list'),
    re_path('^region/(?P<pk>\d+)/$',RegionDetailView.as_view(),name='region-detail'),
    re_path('^region/create/$',RegionCreateView.as_view(),name='region-create'),
    re_path('^region/update/(?P<pk>\d+)/$',RegionUpdateView.as_view(),name='region-update'),
    re_path('^region/delete/(?P<pk>\d+)/$',RegionDeleteView.as_view(),name='region-delete'),
    #Service
    re_path('^service/$',ServiceListView.as_view(),name='service-list'),
    re_path('^service/(?P<pk>\d+)/$',ServiceDetailView.as_view(),name='service-detail'),
    re_path('^service/create/$',ServiceCreateView.as_view(),name='service-create'),
    re_path('^service/update/(?P<pk>\d+)/$',ServiceUpdateView.as_view(),name='service-update'),
    re_path('^service/delete/(?P<pk>\d+)/$',ServiceDeleteView.as_view(),name='service-delete'),
    #Status
    re_path('^status/$',StatusListView.as_view(),name='status-list'),
    re_path('^status/(?P<pk>\d+)/$',StatusDetailView.as_view(),name='status-detail'),
    re_path('^status/create/$',StatusCreateView.as_view(),name='status-create'),
    re_path('^status/update/(?P<pk>\d+)/$',StatusUpdateView.as_view(),name='status-update'),
    re_path('^status/delete/(?P<pk>\d+)/$',StatusDeleteView.as_view(),name='status-delete'),
    #Withdrawal
    re_path('^withdrawal/$',WithdrawalListView.as_view(),name='withdrawal-list'),
    re_path('^withdrawal/(?P<pk>\d+)/$',WithdrawalDetailView.as_view(),name='withdrawal-detail'),
    re_path('^withdrawal/create/$',WithdrawalCreateView.as_view(),name='withdrawal-create'),
    re_path('^withdrawal/update/(?P<pk>\d+)/$',WithdrawalUpdateView.as_view(),name='withdrawal-update'),
    re_path('^withdrawal/delete/(?P<pk>\d+)/$',WithdrawalDeleteView.as_view(),name='withdrawal-delete'),

]