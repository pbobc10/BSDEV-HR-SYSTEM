from django.urls import reverse_lazy
from ..models.regions_models import Region
from ..forms.regions_forms import RegionForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class RegionView(TemplateView):
    template_name = 'hrSystem/region.html'

class RegionListView(ListView):
    model = Region
    context_object_name = 'regions'

class RegionDetailView(DetailView):
    model = Region
    context_object_name = 'region_detail'
    template_name = ''

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm

class RegionDeleteView(DeleteView):
    model = Region
    success_url = reverse_lazy('hrSystem:region-list')
    template_name = 'hrSystem/region_delete.html'