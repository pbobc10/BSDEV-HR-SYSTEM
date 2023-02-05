from django.forms import ModelForm,TextInput
from ..models.regions_models import Region

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        widgets = {
            'region_name':TextInput(attrs={'class':'form-control'}),
        } 
