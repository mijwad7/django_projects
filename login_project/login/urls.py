from . import views
from django.urls import path

app_name = 'login'
urlpatterns = [
    path('', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('signout/', views.signout, name="signout")
]