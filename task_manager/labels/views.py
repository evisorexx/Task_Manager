# Django imports
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Local imports
from .models import Label


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


class BaseLabel(SuccessMessageMixin, LoginRequiredMixin):
    model = Label
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('labels_list')
    fields = ['name']


class LabelsListView(BaseLabel, ListView):
    template_name = 'labels/list.html'
    context_object_name = 'labels'


class CreateLabelView(BaseLabel, CreateView):
    template_name = 'labels/create.html'
    success_message = _("Label successfully created!")


class UpdateLabelView(BaseLabel, UpdateView):
    template_name = 'labels/update.html'
    success_message = _("Label successfully updated!")


class DeleteLabelView(BaseLabel, DeleteView):
    template_name = 'labels/delete.html'
    success_message = _("Label successfully deleted!")

    @handle_protected_error
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
