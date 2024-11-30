from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Task name'))
    description = models.TextField(max_length=1000, blank=True,
                                   verbose_name=_('Description')
                                   )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='executor',
        verbose_name=_('Executor'),
    )
    status = models.ForeignKey(Status, 
                               on_delete=models.PROTECT, null=True,
                               verbose_name=_('Status'))
    labels = models.ManyToManyField(
        Label,
        related_name='label',
        blank=True,
        through='TasksToLabels',
        verbose_name=_('Labels')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TasksToLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

