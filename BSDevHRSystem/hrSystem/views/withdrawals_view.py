from django.urls import reverse_lazy
from ..models.withdrawals_models import Withdrawal
from ..forms.withdrawals_forms import WithdrawalForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class WithdrawalView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/withdrawal.html'

class WithdrawalListView(LoginRequiredMixin,ListView):
    model = Withdrawal
    context_object_name = 'withdrawals'

class WithdrawalDetailView(LoginRequiredMixin,DetailView):
    model = Withdrawal
    context_object_name = 'withdrawal_detail'
    template_name = ''

class WithdrawalCreateView(LoginRequiredMixin,CreateView):
    model = Withdrawal
    form_class = WithdrawalForm

class WithdrawalUpdateView(LoginRequiredMixin,UpdateView):
    model = Withdrawal
    form_class = WithdrawalForm

class WithdrawalDeleteView(LoginRequiredMixin,DeleteView):
    model = Withdrawal
    success_url = reverse_lazy('hrSystem:withdrawal-list')
    template_name = 'hrSystem/withdrawal_delete.html'