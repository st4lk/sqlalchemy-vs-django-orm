from django.urls import path

from . import views


urlpatterns = [
    path("sessions/m1/", views.active_record_example),
]
