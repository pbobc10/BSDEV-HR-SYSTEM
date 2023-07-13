from django.forms import ModelForm,TextInput,Textarea
from ..models.withdrawals_models import Withdrawal

class WithdrawalForm(ModelForm):
    class Meta:
        model = Withdrawal
        fields = '__all__'
        widgets = {
            'withdrawal_name':TextInput(attrs={'class':'form-control text-capitalize','type':'text'}),
            'withdrawal_amount':TextInput(attrs={'class':'form-control text-capitalize','type':'number'}),
            'description':Textarea(attrs={'class':'form-control'}),
        }