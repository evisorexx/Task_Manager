from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import NewUserForm, UpdateUserForm


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


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = _('User updated successfully!')


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_message = _('User deleted successfully!')
    success_url = reverse_lazy('users_list')