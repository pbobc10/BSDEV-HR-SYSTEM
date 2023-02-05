from django.urls import reverse_lazy
from ..models.mouvements_models import Mouvement
from ..forms.mouvements_forms import MouvementForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class MouvementView(TemplateView):
    template_name = 'hrSystem/mouvement.html'

class MouvementListView(ListView):
    model = Mouvement
    context_object_name = 'mouvements'

class MouvementDetailView(DetailView):
    model = Mouvement
    context_object_name = 'mouvement_detail'
    template_name = ''

class MouvementCreateView(CreateView):
    model = Mouvement
    form_class = MouvementForm

class MouvementUpdateView(UpdateView):
    model = Mouvement
    form_class = MouvementForm

class MouvementDeleteView(DeleteView):
    model = Mouvement
    success_url = reverse_lazy('hrSystem:mouvement-list')
    template_name = 'hrSystem/mouvement_delete.html'