from . import views
from django.urls import path

urlpatterns = [
    path("", views.master,name="master")
]