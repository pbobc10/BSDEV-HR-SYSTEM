from django.forms import ModelForm,TextInput,Select
from ..models.services_models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'service_name':TextInput(attrs={'class':'form-control'}),
            'departement_id':Select(attrs={'class':'form-control'}),
        }