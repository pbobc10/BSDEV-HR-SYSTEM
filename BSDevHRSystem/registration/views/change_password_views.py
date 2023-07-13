from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from ..forms.change_password_forms import ChangePasswordForm


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('accounts:login')