from django.forms import ModelForm,TextInput, Textarea
from  ..models.assurances_models import Assurance

class AssuranceForm(ModelForm):

    class Meta:
        model = Assurance
        fields = '__all__'
        widgets = {
            'assurance_type':TextInput(attrs={'class':'form-control'}),
            'description':Textarea(attrs={'class':'form-control','cols':60,'rows':3}),
        }
