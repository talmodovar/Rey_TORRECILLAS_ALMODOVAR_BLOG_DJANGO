# blog/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.post_list, name='post_list'),  # Liste des articles
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Détails de l'article
    path('post/create/', views.create_post, name='create_post'),  # Créer un article
    path('post/<int:id>/comment/create/', views.add_comment, name='add_comment'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('comment/<int:id>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:id>/delete/', views.delete_comment, name='delete_comment'),
]
    