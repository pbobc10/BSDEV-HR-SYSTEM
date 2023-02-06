from django.forms import ModelForm,TextInput,Textarea
from ..models.withdrawals_models import Withdrawal

class WithdrawalForm(ModelForm):
    class Meta:
        model = Withdrawal
        fields = '__all__'
        widgets = {
            'withdrawal_name':TextInput(attrs={'class':'form-control'}),
            'withdrawal_amount':TextInput(attrs={'class':'form-control'}),
            'description':Textarea(attrs={'class':'form-control'}),
        }