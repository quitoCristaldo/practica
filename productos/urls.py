from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('', views.lista_prod, name='lista_prod'),
]