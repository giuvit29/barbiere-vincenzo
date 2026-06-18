from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("prenota/", views.prenota, name="prenota"),
    path("prenotazioni/", views.prenotazioni, name="prenotazioni"),
    path("elimina/<int:id>/", views.elimina_prenotazione, name="elimina"),
    path("completa/<int:id>/", views.completa_prenotazione, name="completa"),
]