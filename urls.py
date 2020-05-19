from django.urls import path

from . import views

urlpatterns = [
    path('show_form', views.show_form, name="show_form"),
]
