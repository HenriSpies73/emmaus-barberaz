from django import forms
from .models import Adherent

class AdherentForm(forms.ModelForm):
    class Meta:
        model = Adherent
        fields = ['nom', 'prenom', 'ville', 'email', 'association']