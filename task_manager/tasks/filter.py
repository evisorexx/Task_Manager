import django_filters
from task_manager.labels.models import Label
from .models import Task
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    def task_by_myself(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    my_tasks = django_filters.BooleanFilter(
        method='task_by_myself',
        widget=forms.CheckboxInput,
        label=_('Show own tasks'),
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label filter'),
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )

    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'executor': ['exact'],
            'labels': ['exact']
        }
