from django.urls import reverse_lazy
from ..models.statuses_models import Status
from ..forms.statuses_forms import StatusForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class StatusView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/status.html'

class StatusListView(LoginRequiredMixin,ListView):
    model = Status
    context_object_name = 'statuss'

class StatusDetailView(LoginRequiredMixin,DetailView):
    model = Status
    context_object_name = 'status_detail'
    template_name = ''

class StatusCreateView(LoginRequiredMixin,CreateView):
    model = Status
    form_class = StatusForm

class StatusUpdateView(LoginRequiredMixin,UpdateView):
    model = Status
    form_class = StatusForm

class StatusDeleteView(LoginRequiredMixin,DeleteView):
    model = Status
    success_url = reverse_lazy('hrSystem:status-list')
    template_name = 'hrSystem/status_delete.html'