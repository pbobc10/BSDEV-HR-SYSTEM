from django.urls import reverse_lazy
from ..models.departements_models import Departement
from ..forms.departements_forms import DepartementForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class DepartementView(TemplateView):
    template_name = 'hrSystem/departement.html'

class DepartementListView(ListView):
    model = Departement
    context_object_name = 'departements'

class DepartementDetailView(DetailView):
    model = Departement
    context_object_name = 'departement_detail'
    template_name = ''

class DepartementCreateView(CreateView):
    model = Departement
    form_class = DepartementForm

class DepartementUpdateView(UpdateView):
    model = Departement
    form_class = DepartementForm

class DepartementDeleteView(DeleteView):
    model = Departement
    success_url = reverse_lazy('hrSystem:departement-list')
    template_name = 'hrSystem/departement_delete.html'