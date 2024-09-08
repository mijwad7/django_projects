from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('add_entry', views.add_entry, name="add_entry"),
    path('edit_entry/<int:id>', views.edit_entry, name="edit_entry"),
    path('delete_entry/<int:id>', views.delete_entry, name="delete_entry"),
]