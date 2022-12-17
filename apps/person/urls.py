from django.urls import path

from . import views

app_name = 'person'

urlpatterns = [
    path('', views.RegisterPersonView.as_view(), name='register'),
    path('listagem/', views.ListPersonView.as_view(), name='listing'),
    path(
        'atualizar/<int:pk>', views.UpdatePersonView.as_view(), name='update'
    ),
]
