from django.db import models

# Create your models here.

class Association(models.Model):
    nom = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Adherent(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    date_adhesion = models.DateField(auto_now_add=True)
    association = models.ForeignKey(Association, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.prenom + " " + self.nom