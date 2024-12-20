from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User


class AuthView(SuccessMessageMixin, LoginView):
    model = User
    template_name = 'login.html'
    fields = ['first_name', 'last_name', 'username', 'password']
    success_message = _('You are logged in!')


class ExitView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _('You are logged out!'))
        return response
