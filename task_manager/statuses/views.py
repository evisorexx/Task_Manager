from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .mixins import StatusMixin, handle_protected_error


class StatusListView(StatusMixin, ListView):
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'


class StatusCreateView(StatusMixin, CreateView):
    template_name = 'statuses/create.html'
    success_message = _("Status successfully created!")


class StatusUpdateView(StatusMixin, UpdateView):
    template_name = 'statuses/update.html'
    success_message = _("Status successfully updated!")


class StatusDeleteView(StatusMixin, DeleteView):
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
