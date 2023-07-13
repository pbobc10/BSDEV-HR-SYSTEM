from django.urls import reverse_lazy
from ..models.mouvements_models import Mouvement
from ..forms.mouvements_forms import MouvementForm
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

class MouvementView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,TemplateView):
    template_name = 'hrSystem/mouvement.html'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class MouvementListView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,ListView):
    model = Mouvement
    context_object_name = 'mouvements'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class MouvementDetailView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DetailView):
    model = Mouvement
    context_object_name = 'mouvement_detail'
    template_name = ''
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager', 'Hr']
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))

class MouvementCreateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,CreateView):
    model = Mouvement
    form_class = MouvementForm
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager',]
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Mouvement successfully created')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Mouvement creation failed')
        return super().form_invalid(form)

class MouvementUpdateView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,UpdateView):
    model = Mouvement
    form_class = MouvementForm
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager',]
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Mouvement successfully updated')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Mouvement update failed')
        return super().form_invalid(form)

class MouvementDeleteView(LoginRequiredMixin,UserPassesTestMixin,GroupRequiredMixin,DeleteView):
    model = Mouvement
    success_url = reverse_lazy('hrSystem:mouvement-list')
    template_name = 'hrSystem/mouvement_delete.html'
    # URL to redirect if user is not authenticated
    login_url = 'hrSystem:login'
    # Group required to access the view
    group_required = ['Admin','Manager',]
    

    def test_func(self):
        #condition to check if the user's groups match any of the required groups
        return self.request.user.groups.filter(name__in=self.group_required).exists()
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.warning(self.request, 'You are not allowed to access this page!')
        return HttpResponseRedirect(reverse_lazy('hrSystem:leave-list'))
    
    def form_valid(self,form):
        messages.success(self.request, 'Mouvement successfully deleted')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, 'Mouvement deletion failed')
        return super().form_invalid(form)