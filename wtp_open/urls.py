from django.urls import path
from . import views

urlpatterns = [
    path('', views.wtp_open),
]