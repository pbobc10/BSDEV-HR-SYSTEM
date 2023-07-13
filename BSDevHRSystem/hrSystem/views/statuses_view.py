from django.urls import reverse_lazy
from ..models.statuses_models import Status
from ..forms.statuses_forms import StatusForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from braces.views import GroupRequiredMixin
from django.http.response import HttpResponseRedirect
from django.contrib import messages

class StatusView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,TemplateView):
    template_name = 'hrSystem/status.html'
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

class StatusListView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,ListView):
    model = Status
    context_object_name = 'statuss'
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

class StatusDetailView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DetailView):
    model = Status
    context_object_name = 'status_detail'
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

class StatusCreateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,CreateView):
    model = Status
    form_class = StatusForm
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
        messages.success(self.request, 'Status successfully created')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Status creation failed')
        return super().form_invalid(form)


class StatusUpdateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,UpdateView):
    model = Status
    form_class = StatusForm
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
        messages.success(self.request, 'Status successfully updated')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Status update failed')
        return super().form_invalid(form)


class StatusDeleteView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DeleteView):
    model = Status
    success_url = reverse_lazy('hrSystem:status-list')
    template_name = 'hrSystem/status_delete.html'
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
        messages.success(self.request, 'Status successfully deleted')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Status deletion failed')
        return super().form_invalid(form)
