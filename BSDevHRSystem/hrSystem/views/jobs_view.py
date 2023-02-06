from django.urls import reverse_lazy
from ..models.jobs_models import Job
from ..forms.jobs_forms import JobForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class JobView(LoginRequiredMixin,TemplateView):
    template_name = 'hrSystem/job.html'

class JobListView(LoginRequiredMixin,ListView):
    model = Job
    context_object_name = 'jobs'

class JobDetailView(LoginRequiredMixin,DetailView):
    model = Job
    context_object_name = 'job_detail'
    template_name = ''

class JobCreateView(LoginRequiredMixin,CreateView):
    model = Job
    form_class = JobForm

class JobUpdateView(LoginRequiredMixin,UpdateView):
    model = Job
    form_class = JobForm

class JobDeleteView(LoginRequiredMixin,DeleteView):
    model = Job
    success_url = reverse_lazy('hrSystem:job-list')
    template_name = 'hrSystem/job_delete.html'