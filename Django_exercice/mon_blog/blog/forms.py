# blog/forms.py
from django import forms
from .models import Comment
from .models import BlogPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']  # Champs à afficher dans le formulaire


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']  # Spécifie les champs à inclure dans le formulaire
        
