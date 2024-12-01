from django.urls import path

from . import views

urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks_list'),
    path('create/', views.CreateTaskView.as_view(), name='task_create'),
    path('<int:pk>/', views.TaskDetailsView.as_view(), name='task_details'),
    path(
        '<int:pk>/update/',
        views.UpdateTaskView.as_view(),
        name='task_update'
    ),
    path(
        '<int:pk>/delete/',
        views.DeleteTaskView.as_view(),
        name='task_delete'
    ),
]
