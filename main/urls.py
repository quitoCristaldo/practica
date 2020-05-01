from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),   
]