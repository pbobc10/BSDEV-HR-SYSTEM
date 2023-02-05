from django.urls import reverse_lazy
from ..models.jobs_models import Job
from ..forms.jobs_forms import JobForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView

class JobView(TemplateView):
    template_name = 'hrSystem/job.html'

class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'

class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job_detail'
    template_name = ''

class JobCreateView(CreateView):
    model = Job
    form_class = JobForm

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm

class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('hrSystem:job-list')
    template_name = 'hrSystem/job_delete.html'