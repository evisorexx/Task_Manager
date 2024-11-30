from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Task
from .filter import TaskFilter


class BaseTask(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('tasks_list')
    fields = ['name', 'description', 'executor', 'status', 'labels']


class TasksListView(BaseTask, FilterView):
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskDetailsView(BaseTask, DetailView):
    template_name = 'tasks/details.html'
    context_object_name = 'task'


class CreateTaskView(BaseTask, CreateView):
    template_name = 'tasks/create.html'
    context_object_name = 'tasks'
    success_message = _('Task successfully created!')

    # Redefine form_valid from ModelFormMixin
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(BaseTask, UpdateView):
    template_name = 'tasks/update.html'
    success_message = _('Task successfully updated!')


class DeleteTaskView(BaseTask, DeleteView):
    template_name = 'tasks/delete.html'
    success_message = _('Task successfully deleted!')

    def has_permission(self):
        obj = self.get_object()
        return obj is not None and obj.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authenticated.'))
            return self.handle_no_permission()

        elif self.has_permission():
            messages.error(
                request,
                _("Only authors can delete their own tasks.")
            )
            return redirect('tasks_list')
        return super().dispatch(request, *args, **kwargs)