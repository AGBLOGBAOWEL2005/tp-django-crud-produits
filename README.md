Markdown

Application de Gestion de Produits (Django CRUD)
Cette application web développée avec Django permet de gérer un catalogue de produits organisés par catégories. Elle implémente les fonctionnalités complètes de création, lecture, mise à jour et suppression (CRUD).

Fonctionnalités
Gestion des Catégories
Liste, ajout, modification et suppression des catégories.
Suppression en cascade (si une catégorie est supprimée, ses produits le sont aussi).
Gestion des Produits
Liste paginée (5 produits par page).
Ajout et modification avec sélection dynamique de la catégorie.
Formatage des prix et gestion des stocks (quantité).
Interface Utilisateur
Design responsive basé sur Bootstrap.
Navigation fluide entre les produits et les catégories.
Persistance de l'état isAdmin (localStorage) pour l'affichage conditionnel des boutons d'action.
🛠️ Installation et Lancement
1. Cloner le projet
git clone <url-du-depot>
cd <nom-du-dossier>
2. Créer un environnement virtuel
Bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Linux/Mac
source venv/bin/activate
3. Installer les dépendances
Bash
pip install -r requirements.txt
4. Appliquer les migrations
Bash
python manage.py makemigrations
python manage.py migrate
5. Créer un compte administrateur (pour l'interface Django Admin)
Bash
python manage.py createsuperuser
6. Lancer le serveur
Bash
python manage.py runserver
L'application sera accessible sur : http://127.0.0.1:8000/
