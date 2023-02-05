from django.urls import reverse_lazy
from ..models.assurances_models import Assurance
from ..forms.assurances_forms import AssuranceForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class AssuranceView(TemplateView):
    template_name = 'hrSystem/assurance.html'

class AssuranceListView(ListView):
    model = Assurance
    context_object_name = 'assurances'

class AssuranceDetailView(DetailView):
    model = Assurance
    context_object_name = 'assurance_detail'
    template_name = ''

class AssuranceCreateView(CreateView):
    model = Assurance
    form_class = AssuranceForm

class AssuranceUpdateView(UpdateView):
    model = Assurance
    form_class = AssuranceForm

class AssuranceDeleteView(DeleteView):
    model = Assurance
    success_url = reverse_lazy('hrSystem:assurance-list')
    template_name = 'hrSystem/assurance_delete.html'