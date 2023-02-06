from django.urls import reverse_lazy
from ..models.mouvements_models import Mouvement
from ..forms.mouvements_forms import MouvementForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MouvementView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/mouvement.html'

class MouvementListView(LoginRequiredMixin,ListView):
    model = Mouvement
    context_object_name = 'mouvements'

class MouvementDetailView(LoginRequiredMixin,DetailView):
    model = Mouvement
    context_object_name = 'mouvement_detail'
    template_name = ''

class MouvementCreateView(LoginRequiredMixin,CreateView):
    model = Mouvement
    form_class = MouvementForm

class MouvementUpdateView(LoginRequiredMixin,UpdateView):
    model = Mouvement
    form_class = MouvementForm

class MouvementDeleteView(LoginRequiredMixin,DeleteView):
    model = Mouvement
    success_url = reverse_lazy('hrSystem:mouvement-list')
    template_name = 'hrSystem/mouvement_delete.html'