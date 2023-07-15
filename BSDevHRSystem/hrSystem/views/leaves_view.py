from typing import Optional, Type
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from ..models.leaves_models import Leave
from ..models.employees_models import Employee
from ..forms.leaves_forms import LeaveForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from braces.views import GroupRequiredMixin
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from  csv import writer
from django.http import JsonResponse,HttpResponse
from datetime import datetime

class LeaveView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,TemplateView):
    template_name = 'hrSystem/leave.html'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr','Employee']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class LeaveListView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,ListView):
    model = Leave
    context_object_name = 'leaves'
    
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr','Employee']
    
    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    # the get_queryset method is overridden to return the queryset of leaves based on the employee
    def get_queryset(self):
        if self.request.user.groups.filter(name__in= ['Admin','Manager']).exists():
            return Leave.objects.all()
        else:
            return Leave.objects.filter(employee=Employee.objects.get(user=self.request.user))

class LeaveDetailView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DetailView):
    model = Leave
    context_object_name = 'leave_detail'
    template_name = ''
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr','Employee']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class LeaveCreateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,CreateView):
    model = Leave
    form_class = LeaveForm
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager','Hr','Employee']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        # Prevent employee to submit a new leave if he got a pending one
        if Leave.objects.filter(employee=Employee.objects.get(user=self.request.user),status='PENDING').exists():
            messages.warning(self.request, 'You cannot submit a new leave if you had one pendind')
            return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
        else:
            form.instance.employee =Employee.objects.get(user=self.request.user) 
            messages.success(self.request, 'Leave successfully created')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Leave creation failed')
        return super().form_invalid(form)
    
    # the get_form method is overridden to return the form based on the model
    # its used here to modify the form fields (status and can_edit)
    def get_form(self, form_class=None):
        form= super().get_form(form_class)
        if not self.request.user.groups.filter(name__in=['Admin','Manager']).exists():
            form.fields.pop('status')
            form.fields.pop('can_edit')
        return form
    
class LeaveUpdateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,UpdateView):
    model = Leave
    form_class = LeaveForm
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager','Hr','Employee']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Leave successfully updated')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Leave update failed')
        return super().form_invalid(form)

class LeaveDeleteView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DeleteView):
    model = Leave
    success_url = reverse_lazy('hrSystem:leave-list')
    template_name = 'hrSystem/leave_delete.html'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager','Hr','Employee']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Leave successfully deleted')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Leave deletion failed')
        return super().form_invalid(form)