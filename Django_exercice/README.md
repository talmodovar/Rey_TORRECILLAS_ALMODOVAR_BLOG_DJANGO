

Créé par : Lucas REY TORREICILLAS et Thomas ALMODOVAR*

### Instructions de mise en place ###

## 1 Télécharger python 

A cette adresse : https://www.python.org/downloads/ 

Cocher “AJOUTER AU PATH” lors de l’installation 

 

 

## 2 Set up le projet et l’appli 

    Ouvrir CMD 

        - pip install django 

        - cd 'Chemin d'acces du projet'

        - python manage.py makemigrations blog

        - python manage.py migrate

        

    

 

## 3 Lancements du serveur + consultation 

    LANCER LE SERVEUR : python manage.py runserver  

    Adresse de consultation : http://127.0.0.1:8000/blog






### Mini Blog Application ###

## Description

Application de blog permettant de créer, éditer, consulter et supprimer des articles et des commentaires.
Fonctionnalités

    Articles : Créer, voir, éditer, supprimer.
    Commentaires : Ajouter, éditer, supprimer.
    Navigation : Layout commun avec liens pour gérer les posts et commentaires.

## URLs

    /: Liste des articles.
    /post/<id>/: Détail de l'article.
    /post/create/: Créer un article.
    /post/<id>/edit/: Éditer un article.
    /post/<id>/add_comment/: Ajouter un commentaire.
    /comment/<id>/edit/: Éditer un commentaire.
    /post/<id>/delete/: Supprimer un article.
    /comment/<id>/delete/: Supprimer un commentaire.

## Tests

Assurer le bon fonctionnement des actions sur les articles et commentaires, ainsi que des redirections et affichages.