from django.urls import reverse_lazy
from ..models.services_models import Service
from ..forms.services_forms import ServiceForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ServiceView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/service.html'

class ServiceListView(LoginRequiredMixin,ListView):
    model = Service
    context_object_name = 'services'

class ServiceDetailView(LoginRequiredMixin,DetailView):
    model = Service
    context_object_name = 'service_detail'
    template_name = ''

class ServiceCreateView(LoginRequiredMixin,CreateView):
    model = Service
    form_class = ServiceForm

class ServiceUpdateView(LoginRequiredMixin,UpdateView):
    model = Service
    form_class = ServiceForm

class ServiceDeleteView(LoginRequiredMixin,DeleteView):
    model = Service
    success_url = reverse_lazy('hrSystem:service-list')
    template_name = 'hrSystem/service_delete.html'