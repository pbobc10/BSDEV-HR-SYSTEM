from django.urls import reverse_lazy
# from ..models.banks_models import Bank
# from ..forms.banks_forms import BankForm
from django.views.generic import TemplateView #,ListView,DetailView,UpdateView,DeleteView,CreateView

class DashboardView(TemplateView):
    template_name = 'hrSystem/dashboard.html'

