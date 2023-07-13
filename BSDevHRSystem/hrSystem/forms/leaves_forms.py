from typing import Any
from django.forms import ModelForm,TextInput,DateInput,EmailInput,NumberInput,Select,DateField
from ..models.leaves_models import Leave
from django.core.validators import ValidationError


class LeaveForm(ModelForm):
    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date > end_date:
            raise ValidationError("Start date must be less than end date")
        return cleaned_data

    class Meta:
        model = Leave
        # exclude = ('employee_id',)
        fields = '__all__'
        labels = {
            'comment': '',
        }
        widgets = {
            'employee_id':Select(attrs={'class':'form-control'}),
            'start_date':DateInput(attrs={'class':'form-control','type': 'date'}),
            'end_date':DateInput(attrs={'class':'form-control','type': 'date'}),
            'reason':Select(attrs={'class':'form-control'}),
            'comment':TextInput(attrs={'class':'form-control','placeholder': 'Enter value here...'}),
            
        }
        