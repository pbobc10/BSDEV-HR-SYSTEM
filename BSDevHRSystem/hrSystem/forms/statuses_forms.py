from django.forms import ModelForm,TextInput
from ..models.statuses_models import Status

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        widgets = {
            'status_type':TextInput(attrs={'class':'form-control text-uppercase','type':'text'}),
        }