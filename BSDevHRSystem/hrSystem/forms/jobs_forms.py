from django.forms import ModelForm,TextInput
from ..models.jobs_models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'job_title':TextInput(attrs={'class':'form-control'}),
            'salary':TextInput(attrs={'class':'form-control'}),
        }