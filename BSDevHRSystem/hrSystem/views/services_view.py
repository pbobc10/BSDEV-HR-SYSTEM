from django.urls import reverse_lazy
from ..models.services_models import Service
from ..forms.services_forms import ServiceForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class ServiceView(TemplateView):
    template_name = 'hrSystem/service.html'

class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service_detail'
    template_name = ''

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm

class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('hrSystem:service-list')
    template_name = 'hrSystem/service_delete.html'