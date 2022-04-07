from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("new_infusion", views.new_infusion),
]