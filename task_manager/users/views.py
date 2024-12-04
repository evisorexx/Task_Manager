from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import NewUserForm, UpdateUserForm
from .mixins import PermissionMixin
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'


class UserCreationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully!')


class UserUpdateView(PermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = _('User updated successfully!')


class UserDeleteView(PermissionMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_message = _('User deleted successfully!')
    success_url = reverse_lazy('users_list')
