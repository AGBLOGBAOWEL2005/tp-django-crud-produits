from django.shortcuts import render, redirect, get_object_or_404
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Produit.models import Produit,Categorie
from django.db.models import Q
# Create your views here.
def acceuil(request):
    return  render(request,'Produit/acceuil.html')

def liste(request):
    query = request.GET.get('search')

    if query:
        produits = Produit.objects.filter(
            Q(libelle__icontains=query) |
            Q(categorie__libelle__icontains=query)
        ).select_related('categorie').order_by('-dateCreation')
    else:
        produits = Produit.objects.all().select_related('categorie').order_by('-dateCreation')

    categories = Categorie.objects.all()

    paginator = Paginator(produits, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Produit/liste.html', {
        'produits': page_obj,
        'categories': categories,
        'search_query': query
    })
def addProduit(request):
    if request.method == 'POST':
        libelle = request.POST['libelle']
        prix = request.POST['prix']
        quantite = request.POST['quantite']
        id_categorie = request.POST.get('categorie')
        categorie_instance = Categorie.objects.get(id=id_categorie)
        Produit.objects.create(libelle=libelle,prix=prix,quantite=quantite,categorie=categorie_instance)
    return redirect('liste')
def ajout(request):
    categories = Categorie.objects.all()
    return render(request, 'Produit/ajout.html', {'categories': categories})

def deleteProduit(request,id):
    produit = get_object_or_404(Produit,id=id)
    produit.delete()
    return redirect('liste')

def modifProduit(request,id):
    produit = get_object_or_404(Produit,id=id)
    categories = Categorie.objects.all()
    return render(request,'Produit/update.html',{'produit':produit,'categories': categories})
def updateProduit(request):
    if request.POST:
        produit = get_object_or_404(Produit,id=request.POST['id'])
        produit.libelle = request.POST['libelle']
        produit.prix = float(request.POST['prix'].replace(',', '.'))
        produit.quantite = float(request.POST['quantite'].replace(',', '.'))
        id_cat = request.POST.get('categorie')
        produit.categorie = Categorie.objects.get(id=id_cat)
        produit.save()
    return redirect('liste')

def choixCategorie(request):
    # On récupère toutes les catégories pour le menu déroulant
    categories = Categorie.objects.all()
    return render(request, 'Produit/ajout.html', {'categories': categories})


#Categorie

def listeCategorie(request):
    categories = Categorie.objects.all()
    return render(request, 'Produit/listCat.html', {'cats': categories})

def addCategorie(request):
    if request.method == 'POST':
        libelle = request.POST['libelle']
        description = request.POST['description']
        Categorie.objects.create(libelle=libelle,description=description)
    return redirect("listeCat")

def deleteCategorie(request,id):
    categorie = get_object_or_404(Categorie,id=id)
    categorie.delete()
    return redirect("listeCat")

def modifCategorie(request,id):
    categorie = get_object_or_404(Categorie,id=id)
    return render(request,'Produit/updateCat.html',{'cat':categorie})

def updateCategorie(request):
    if request.method == 'POST':
        categorie = get_object_or_404(Categorie,id=request.POST['id'])
        categorie.libelle = request.POST['libelle']
        categorie.description = request.POST['description']
        categorie.save()
    return redirect("listeCat")
