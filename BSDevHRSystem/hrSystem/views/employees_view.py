from django.urls import reverse_lazy
from ..models.employees_models import Employee
from ..forms.employees_forms import EmployeeForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class EmployeeView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/employee.html'

class EmployeeListView(LoginRequiredMixin,ListView):
    model = Employee
    context_object_name = 'employees'

class EmployeeDetailView(LoginRequiredMixin,DetailView):
    model = Employee
    context_object_name = 'employee_detail'
    template_name = ''

class EmployeeCreateView(LoginRequiredMixin,CreateView):
    model = Employee
    form_class = EmployeeForm

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model = Employee
    form_class = EmployeeForm

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model = Employee
    success_url = reverse_lazy('hrSystem:employee-list')
    template_name = 'hrSystem/employee_delete.html'