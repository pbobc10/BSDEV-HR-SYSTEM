from django.forms import ModelForm,TextInput,DateInput,EmailInput,NumberInput,Select
from ..models.employees_models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ('employe_id',)
        
        widgets = {
            'employe_id':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control'}),
            'first_name':TextInput(attrs={'class':'form-control'}),
            'sex':Select(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
            'cin':NumberInput(attrs={'class':'form-control'}),
            'nif':TextInput(attrs={'class':'form-control'}),
            'phone1':TextInput(attrs={'class':'form-control'}),
            'phone2':TextInput(attrs={'class':'form-control'}),
            'birth_date':DateInput(attrs={'class':'form-control'}),
            'hire_date':DateInput(attrs={'class':'form-control'}),
            #'salary':DecimalField(attrs={'class':'form-control'}),
            'manager_id':Select(attrs={'class':'form-control'}),
            'service_id':Select(attrs={'class':'form-control'}),
            'status_id':Select(attrs={'class':'form-control'}),
            'assurance_id':Select(attrs={'class':'form-control'}),
            'job_id':Select(attrs={'class':'form-control'}),
            'bank_id':Select(attrs={'class':'form-control'}),
            'bank_account':TextInput(attrs={'class':'form-control'}),
            'mode_paiement':Select(attrs={'class':'form-control'}),
        }