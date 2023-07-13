from django.urls import reverse_lazy
from ..models.countries_models import Country
from ..forms.crountries_forms import CountryForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.http.response import HttpResponseRedirect

class CountryView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,TemplateView):
    template_name = 'hrSystem/country.html'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class CountryListView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,ListView):
    model = Country
    context_object_name = 'countries'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class CountryDetailView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DetailView):
    model = Country
    context_object_name = 'country_detail'
    template_name = ''
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class CountryCreateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,CreateView):
    model = Country
    form_class = CountryForm
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager',]
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Country successfully created')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Country creation failed')
        return super().form_invalid(form)

class CountryUpdateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,UpdateView):
    model = Country
    form_class = CountryForm
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager',]
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Country successfully updated')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Country update failed')
        return super().form_invalid(form)

class CountryDeleteView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DeleteView):
    model = Country
    success_url = reverse_lazy('hrSystem:country-list')
    template_name = 'hrSystem/country_delete.html'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager',]
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Country successfully deleted')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Country deletion failed')
        return super().form_invalid(form)