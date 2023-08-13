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
from datetime import datetime,date,timedelta

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
    
    def get_context_data(self,**kwars):
        context = super().get_context_data(**kwars)
        context['can_update'] = self.request.user.groups.filter(name__in= ['Admin','Manager']).exists()
        return context


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
        # employee cannot submit a leave if he hasn't had at least one year of work
        employee = Employee.objects.get(user=self.request.user)
        # check if employee has at least one year of work
        if date.today() - employee.hire_date < timedelta(days=365):
            messages.warning(self.request, 'You cannot submit a new leave if you haven\'t had at least one year of work')
            return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
        else:
        # prevent a user from registering a new leave if the period of an approved one has not yet passed
            last_approved_leave = Leave.objects.filter(employee = Employee.objects.get(user=self.request.user),status = 'APPROVED').order_by('-end_date').first()
            if last_approved_leave and last_approved_leave.end_date >= date.today():
                messages.warning(self.request, 'You cannot submit a new leave if the period of an approved one has not yet passed')
                return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
            else :
            # Prevent employee to submit a new leave if he got a pending one
                if Leave.objects.filter(employee=Employee.objects.get(user=self.request.user),status='PENDING').exists():
                    messages.warning(self.request, 'You cannot submit a new leave if you had one pendind')
                    return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
                
                else: # submit the leave
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
        #if not self.request.user.groups.filter(name__in=['Admin','Manager']).exists():
        # when creating a leave, the status is set to pending by default
        form.fields.pop('status')
        form.fields.pop('can_edit')
        form.instance.status = 'PENDING'

        # customize the leave choices based on the gender of the employee
        employee = Employee.objects.get(user=self.request.user)
        if employee.sex == 'M':
            # reassign values to the reason field based on the gender
            form.fields['reason'].choices = [(key,value) for key,value in form.fields['reason'].choices if key != 'MATERNITY' ]
        else:
            form.fields['reason'].choices = [(key,value) for key,value in form.fields['reason'].choices if key != 'PATERNITY' ]
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
    
    def get_form(self, form_class=None):
        form= super().get_form(form_class)
        if not self.request.user.groups.filter(name__in=['Admin','Manager']).exists():
            form.fields.pop('status')
            form.fields.pop('can_edit')
            form.instance.status = 'PENDING'

        # customize the leave choices based on the gender of the employee
        employee = Employee.objects.get(user=self.request.user)
        if employee.sex == 'M':
            # reassign values to the reason field based on the gender
            form.fields['reason'].choices = [(key,value) for key,value in form.fields['reason'].choices if key != 'MATERNITY' ]
        else:
            form.fields['reason'].choices = [(key,value) for key,value in form.fields['reason'].choices if key != 'PATERNITY' ]

        return form
    
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