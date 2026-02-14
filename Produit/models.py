from django.db import models

# Create your models here.

class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Produit(models.Model):
    libelle = models.CharField(max_length=50)
    prix = models.FloatField()
    quantite = models.FloatField()
    dateCreation = models.DateField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self):
        return self.libelle

