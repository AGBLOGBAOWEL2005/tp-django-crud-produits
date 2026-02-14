"""
URL configuration for Projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Produit.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',acceuil,name='acceuil'),
    path('liste/',liste,name='liste'),
    path('ajoutProduit/',addProduit,name='ajoutProduit'),
    path('ajouterProduit/',ajout,name='ajout'),

    path('deleteProduit/<int:id>',deleteProduit,name='supProduit'),
    path('modifProduit/<int:id>',modifProduit,name='modifProduit'),
    path('updateProduit',updateProduit,name='updateProduit'),
    path('choixCategorie',choixCategorie,name='choixCategorie'),

    #categorie
    path('addCategorie/', addCategorie, name='ajoutCategorie'),
    path('listeCat/',listeCategorie,name='listeCat'),

    path('supCategorie/<int:id>', deleteCategorie, name='supCategorie'),
    path('modifCategorie/<int:id>', modifCategorie, name='modifCategorie'),
    path('modiierCat/', updateCategorie, name='modifierCat'),

]
