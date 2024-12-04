from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .models import Label


class LabelMixin(SuccessMessageMixin, LoginRequiredMixin):
    model = Label
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('labels_list')
    fields = ['name']


def handle_protected_error(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            return func(self, request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("Can't delete this label, it is attached to task.")
            )
            return redirect(reverse_lazy('labels_list'))
    return wrapper

