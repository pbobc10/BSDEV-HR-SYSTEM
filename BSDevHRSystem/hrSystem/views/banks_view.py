from django.urls import reverse_lazy
from ..models.banks_models import Bank
from ..forms.banks_forms import BankForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class BankView(TemplateView):
    template_name = 'hrSystem/bank.html'

class BankListView(ListView):
    model = Bank
    context_object_name = 'banks'

class BankDetailView(DetailView):
    model = Bank
    context_object_name = 'bank_detail'
    template_name = ''

class BankCreateView(CreateView):
    model = Bank
    form_class = BankForm

class BankUpdateView(UpdateView):
    model = Bank
    form_class = BankForm

class BankDeleteView(DeleteView):
    model = Bank
    success_url = reverse_lazy('hrSystem:bank-list')
    template_name = 'hrSystem/bank_delete.html'