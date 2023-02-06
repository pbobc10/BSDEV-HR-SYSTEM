from django.urls import reverse_lazy
from ..models.regions_models import Region
from ..forms.regions_forms import RegionForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class RegionView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/region.html'

class RegionListView(LoginRequiredMixin,ListView):
    model = Region
    context_object_name = 'regions'

class RegionDetailView(LoginRequiredMixin,DetailView):
    model = Region
    context_object_name = 'region_detail'
    template_name = ''

class RegionCreateView(LoginRequiredMixin,CreateView):
    model = Region
    form_class = RegionForm

class RegionUpdateView(LoginRequiredMixin,UpdateView):
    model = Region
    form_class = RegionForm

class RegionDeleteView(LoginRequiredMixin,DeleteView):
    model = Region
    success_url = reverse_lazy('hrSystem:region-list')
    template_name = 'hrSystem/region_delete.html'