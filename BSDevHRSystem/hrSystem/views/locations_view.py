from django.urls import reverse_lazy
from ..models.locations_models import Location
from ..forms.locations_forms import LocationForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class LocationView(TemplateView):
    template_name = 'hrSystem/location.html'

class LocationListView(ListView):
    model = Location
    context_object_name = 'locations'

class LocationDetailView(DetailView):
    model = Location
    context_object_name = 'location_detail'
    template_name = ''

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm

class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy('hrSystem:location-list')
    template_name = 'hrSystem/location_delete.html'