from django.forms import ModelForm,TextInput,Select
from ..models.locations_models import Location

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'street_address':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'postal_code':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'city':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'state_province':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'country_id':Select(attrs={'class':'form-control'}),
        }