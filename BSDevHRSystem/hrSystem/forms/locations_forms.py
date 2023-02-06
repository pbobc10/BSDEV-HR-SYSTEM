from django.forms import ModelForm,TextInput,Select
from ..models.locations_models import Location

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'street_address':TextInput(attrs={'class':'form-control'}),
            'postal_code':TextInput(attrs={'class':'form-control'}),
            'city':TextInput(attrs={'class':'form-control'}),
            'state_province':TextInput(attrs={'class':'form-control'}),
            'country_id':Select(attrs={'class':'form-control'}),
        }