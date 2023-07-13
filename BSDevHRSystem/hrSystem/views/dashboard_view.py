from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from datetime import datetime, timedelta, date
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
# from ..models.banks_models import Bank
# from ..forms.banks_forms import BankForm
from ..models.employees_models import Employee
from ..models.departements_models import Departement
from ..models.services_models import Service
from ..models.jobs_models import Job
# ,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.views.generic import TemplateView



class DashboardView(LoginRequiredMixin,UserPassesTestMixin, GroupRequiredMixin,TemplateView):
    template_name = 'hrSystem/dashboard.html'
    #URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_of_employees'] = Employee.objects.count()
        context['employees'] = Employee.objects.all()
        context['employees_birth'] = get_people_with_birthday_in_month(date.today())
        context['number_of_departements'] = Departement.objects.count()
        context['number_of_services'] = Service.objects.count()
        context['number_of_jobs'] = Job.objects.count()
        context['pie_chart'] = pie_chart( context['employees'])
        return context


def get_people_with_birthday_in_month(date):
    """ Returns a list of people who have bithday in the specified month"""
    today = date.today()
    month = today.month
    return Employee.objects.filter(birth_date__month=month)


def pie_chart(employees):
    """
    Creates a pie chart showing the percentage of sex from the Employee Django model.

    Args:
      employees: The Employee Django model.

    Returns:
      A list of the data for the pie chart.
    """
    # Get the number of employees by sex.
    male_employees = employees.filter(sex='M').count()
    female_employees = employees.filter(sex='F').count()

    # Create a list of the data for the pie chart.
    data = [male_employees, female_employees]
    labels = ['Male', 'Female']

    return  labels,data


