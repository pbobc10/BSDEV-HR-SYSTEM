from django.urls import reverse_lazy
from ..models.withdrawals_models import Withdrawal
from ..forms.withdrawals_forms import WithdrawalForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class WithdrawalView(TemplateView):
    template_name = 'hrSystem/withdrawal.html'

class WithdrawalListView(ListView):
    model = Withdrawal
    context_object_name = 'withdrawals'

class WithdrawalDetailView(DetailView):
    model = Withdrawal
    context_object_name = 'withdrawal_detail'
    template_name = ''

class WithdrawalCreateView(CreateView):
    model = Withdrawal
    form_class = WithdrawalForm

class WithdrawalUpdateView(UpdateView):
    model = Withdrawal
    form_class = WithdrawalForm

class WithdrawalDeleteView(DeleteView):
    model = Withdrawal
    success_url = reverse_lazy('hrSystem:withdrawal-list')
    template_name = 'hrSystem/withdrawal_delete.html'