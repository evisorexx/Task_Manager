from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from .filter import TaskFilter
from .mixins import PermissionMixin, TaskMixin


class TasksListView(TaskMixin, FilterView):
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskDetailsView(TaskMixin, DetailView):
    template_name = 'tasks/details.html'
    context_object_name = 'task'


class CreateTaskView(TaskMixin, CreateView):
    template_name = 'tasks/create.html'
    context_object_name = 'tasks'
    success_message = _('Task successfully created!')

    # Redefine form_valid from ModelFormMixin
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(TaskMixin, UpdateView):
    template_name = 'tasks/update.html'
    success_message = _('Task successfully updated!')


class DeleteTaskView(TaskMixin, PermissionMixin, DeleteView):
    template_name = 'tasks/delete.html'
    success_message = _('Task successfully deleted!')

    