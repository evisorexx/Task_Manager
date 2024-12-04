from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .models import Task


class TaskMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('tasks_list')
    fields = ['name', 'description', 'executor', 'status', 'labels']


class PermissionMixin:
    def has_permission(self):
        obj = self.get_object()
        return obj is not None and obj.author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authenticated.'))
            return self.handle_no_permission()

        elif not self.has_permission():
            messages.error(
                request,
                _("Only authors can delete their own tasks.")
            )
            return redirect('tasks_list')
        return super().dispatch(request, *args, **kwargs)
