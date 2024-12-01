from django.urls import path

from . import views

urlpatterns = [
    path('', views.LabelsListView.as_view(), name='labels_list'),
    path('create/', views.CreateLabelView.as_view(), name='label_create'),
    path('<int:pk>/update/',
         views.UpdateLabelView.as_view(),
         name='label_update'
         ),
    path('<int:pk>/delete/',
         views.DeleteLabelView.as_view(),
         name='label_delete'
         ),
]
