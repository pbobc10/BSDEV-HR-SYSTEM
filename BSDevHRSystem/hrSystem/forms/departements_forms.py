from django.forms import ModelForm,TextInput,Select
from ..models.departements_models import Departement

class DepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'
        widgets = {
            'departement_name':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'location_id':Select(attrs={'class':'form-control'}),
            'manager_id' :Select(attrs={'class':'form-control'}),
        }