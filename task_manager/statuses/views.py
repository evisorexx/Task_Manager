from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status


class BaseStatus(SuccessMessageMixin, LoginRequiredMixin):
    model = Status
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('statuses_list')
    fields = ['name']


class StatusListView(BaseStatus, ListView):
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'


class StatusCreateView(BaseStatus, CreateView):
    success_message = _("Status successfully created!")
    template_name = 'statuses/create.html'


class StatusUpdateView(BaseStatus, UpdateView):
    success_message = _("Status successfully updated!")
    template_name = 'statuses/update.html'


class StatusDeleteView(BaseStatus, DeleteView):
    success_message = _("Status successfully deleted!")
    template_name = 'statuses/delete.html'
