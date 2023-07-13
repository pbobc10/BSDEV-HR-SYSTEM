from django.forms import ModelForm, TextInput,Textarea
from ..models.banks_models import Bank

class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        widgets = {
            'bank_code':TextInput(attrs={'class':'form-control text-uppercase','placeholder':'UNI','type':'text'}),
            'routing_number_bank':TextInput(attrs={'class':'form-control','type':'number'}),
            'description':Textarea(attrs={'class':'form-control','cols':60,'rows':3}),
        }
