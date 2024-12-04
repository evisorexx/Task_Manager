from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class PermissionMixin:
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
