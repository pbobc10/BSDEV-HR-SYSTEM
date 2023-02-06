from django.forms import ModelForm,TextInput,Textarea
from ..models.mouvements_models import Mouvement

class MouvementForm(ModelForm):
    class Meta:
        model = Mouvement
        fields = '__all__'
        widgets = {
            'mouvement_type':TextInput(attrs={'class':'form-control'}),
            'description':Textarea(attrs={'class':'form-control','cols':60,'row':3}),
        }