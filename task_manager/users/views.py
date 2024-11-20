from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import NewUserForm, UpdateUserForm

class PermMixin:
    def has_permission(self):
        obj = self.get_object()
        return obj is not None and obj.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized!'))
            return redirect('login')
        
        if not self.has_permission():
            messages.error(request, _('You do not have permission to do this.'))
            return redirect('users_list')
        
        return super().dispatch(request, *args, **kwargs)

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


class UserUpdateView(PermMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = _('User updated successfully!')


class UserDeleteView(PermMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_message = _('User deleted successfully!')
    success_url = reverse_lazy('users_list')