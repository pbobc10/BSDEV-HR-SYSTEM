from django.urls import reverse_lazy
from ..models.employees_models import Employee
from ..forms.employees_forms import EmployeeForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class EmployeeView(TemplateView):
    template_name = 'hrSystem/employee.html'

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee_detail'
    template_name = ''

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('hrSystem:employee-list')
    template_name = 'hrSystem/employee_delete.html'