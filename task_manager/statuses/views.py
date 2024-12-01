from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Status


def handle_protected_error(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            return func(self, request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("Can't delete this status, it is attached to task.")
            )
            return redirect(reverse_lazy('statuses_list'))
    return wrapper


class BaseStatus(SuccessMessageMixin, LoginRequiredMixin):
    model = Status
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('statuses_list')
    fields = ['name']


class StatusListView(BaseStatus, ListView):
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'


class StatusCreateView(BaseStatus, CreateView):
    template_name = 'statuses/create.html'
    success_message = _("Status successfully created!")


class StatusUpdateView(BaseStatus, UpdateView):
    template_name = 'statuses/update.html'
    success_message = _("Status successfully updated!")


class StatusDeleteView(BaseStatus, DeleteView):
    template_name = 'statuses/delete.html'
    success_message = _("Status successfully deleted!")

    @handle_protected_error
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
