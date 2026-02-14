from django.contrib import admin

from Produit.models import Produit


# Register your models here.
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libelle','prix','quantite','dateCreation')
