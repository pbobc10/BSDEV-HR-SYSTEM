from django.forms import ModelForm,TextInput,DateInput,EmailInput,NumberInput,Select
from ..models.employees_models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ('employee_id','user')
        #fields = ('user','employee_id','last_name','first_name','sex','email','cin','nif','phone1','phone2','birth_date','hire_date','manager_id','service_id','status_id','assurance_id','job_id')
        
        
        widgets = {
            'employee_id':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'first_name':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'sex':Select(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control text-lowercase','type':'email'}),
            'cin':NumberInput(attrs={'class':'form-control','type':'number'}),
            'nif':TextInput(attrs={'class':'form-control','type':'text'}),
            'phone1':TextInput(attrs={'class':'form-control','type':'phone'}),
            'phone2':TextInput(attrs={'class':'form-control','type':'phone'}),
            'birth_date':DateInput(attrs={'class':'form-control','type': 'date'}),
            'hire_date':DateInput(attrs={'class':'form-control','type': 'date'}),
            'manager_id':Select(attrs={'class':'form-control'}),
            'service_id':Select(attrs={'class':'form-control'}),
            'status_id':Select(attrs={'class':'form-control'}),
            'assurance_id':Select(attrs={'class':'form-control'}),
            'job_id':Select(attrs={'class':'form-control'}),
            'bank_id':Select(attrs={'class':'form-control'}),
            'bank_account':TextInput(attrs={'class':'form-control','type':'number'}),
            'mode_paiement':Select(attrs={'class':'form-control'}),
        }