from django.urls import reverse_lazy
from ..models.statuses_models import Status
from ..forms.statuses_forms import StatusForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class StatusView(TemplateView):
    template_name = 'hrSystem/status.html'

class StatusListView(ListView):
    model = Status
    context_object_name = 'statuss'

class StatusDetailView(DetailView):
    model = Status
    context_object_name = 'status_detail'
    template_name = ''

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm

class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('hrSystem:status-list')
    template_name = 'hrSystem/status_delete.html'