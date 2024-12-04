from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .mixins import LabelMixin, handle_protected_error


class LabelsListView(LabelMixin, ListView):
    template_name = 'labels/list.html'
    context_object_name = 'labels'


class CreateLabelView(LabelMixin, CreateView):
    template_name = 'labels/create.html'
    success_message = _("Label successfully created!")


class UpdateLabelView(LabelMixin, UpdateView):
    template_name = 'labels/update.html'
    success_message = _("Label successfully updated!")


class DeleteLabelView(LabelMixin, DeleteView):
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
