from django.contrib.auth.forms import UserCreationForm
from .models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data["username"]
        return username


class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data["username"]
        return username
