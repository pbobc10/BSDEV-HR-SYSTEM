from django.urls import reverse_lazy
from ..models.departements_models import Departement
from ..forms.departements_forms import DepartementForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DepartementView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/departement.html'

class DepartementListView(LoginRequiredMixin,ListView):
    model = Departement
    context_object_name = 'departements'

class DepartementDetailView(LoginRequiredMixin,DetailView):
    model = Departement
    context_object_name = 'departement_detail'
    template_name = ''

class DepartementCreateView(LoginRequiredMixin,CreateView):
    model = Departement
    form_class = DepartementForm

class DepartementUpdateView(LoginRequiredMixin,UpdateView):
    model = Departement
    form_class = DepartementForm

class DepartementDeleteView(LoginRequiredMixin,DeleteView):
    model = Departement
    success_url = reverse_lazy('hrSystem:departement-list')
    template_name = 'hrSystem/departement_delete.html'