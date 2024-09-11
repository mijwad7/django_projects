from urllib.parse import urlparse
from . import views
from django.urls import path

app_name = 'login'
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('', views.home, name="home"),
    path('signout/', views.signout_view, name="signout")
]
