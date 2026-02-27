from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_adherents, name='liste_adherents'),
    path('supprimer/<int:id>/', views.supprimer_adherent, name='supprimer_adherent'),
    path('modifier/<int:id>/', views.modifier_adherent, name='modifier_adherent'),
   
]