from django.urls import path

from .views import home, centralidades


urlpatterns = [
    path("", home, name="home"),
    path("centralidades/", centralidades, name="centralidades")
]
