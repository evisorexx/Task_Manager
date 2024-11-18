from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='users_list'),
    path('create/', views.UserCreationView.as_view(), name='users_create'),
    path('<int:pk>/update/', login_required(views.UserUpdateView.as_view()), name='users_update'),
    path('<int:pk>/delete/', login_required(views.UserDeleteView.as_view()), name='users_delete'),
]