from django.urls import reverse_lazy
from ..models.locations_models import Location
from ..forms.locations_forms import LocationForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LocationView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/location.html'

class LocationListView(LoginRequiredMixin,ListView):
    model = Location
    context_object_name = 'locations'

class LocationDetailView(LoginRequiredMixin,DetailView):
    model = Location
    context_object_name = 'location_detail'
    template_name = ''

class LocationCreateView(LoginRequiredMixin,CreateView):
    model = Location
    form_class = LocationForm

class LocationUpdateView(LoginRequiredMixin,UpdateView):
    model = Location
    form_class = LocationForm

class LocationDeleteView(LoginRequiredMixin,DeleteView):
    model = Location
    success_url = reverse_lazy('hrSystem:location-list')
    template_name = 'hrSystem/location_delete.html'