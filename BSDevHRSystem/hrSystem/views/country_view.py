from django.urls import reverse_lazy
from ..models.countries_models import Country
from ..forms.crountries_forms import CountryForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CountryView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/country.html'

class CountryListView(LoginRequiredMixin,ListView):
    model = Country
    context_object_name = 'countries'

class CountryDetailView(LoginRequiredMixin,DetailView):
    model = Country
    context_object_name = 'country_detail'
    template_name = ''

class CountryCreateView(LoginRequiredMixin,CreateView):
    model = Country
    form_class = CountryForm

class CountryUpdateView(LoginRequiredMixin,UpdateView):
    model = Country
    form_class = CountryForm

class CountryDeleteView(LoginRequiredMixin,DeleteView):
    model = Country
    success_url = reverse_lazy('hrSystem:country-list')
    template_name = 'hrSystem/country_delete.html'