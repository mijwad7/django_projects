from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('<int:id>/edit/', views.event_edit, name='event_edit'),
    path('<int:id>/delete/', views.event_delete, name='event_delete'),
]
