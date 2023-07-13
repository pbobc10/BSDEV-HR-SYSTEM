from django.forms import ModelForm,TextInput,Select
from ..models.countries_models import Country

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'country_name':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'region_id':Select(attrs={'class':'form-control'}),
        }