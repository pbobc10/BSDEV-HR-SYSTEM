from django.forms import ModelForm, TextInput,Textarea
from ..models.banks_models import Bank

class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        widgets = {
            'bank_code':TextInput(attrs={'class':'form-control','placeholder':'UNI'}),
            'routing_number_bank':TextInput(attrs={'class':'form-control'}),
            'description':Textarea(attrs={'class':'form-control','cols':60,'rows':3}),
        }
