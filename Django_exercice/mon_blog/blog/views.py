from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm 
from .models import BlogPost, Comment
from .forms import BlogPostForm


def home(request):
    posts = BlogPost.objects.all() 
    return render(request, 'home.html', {'posts': posts})

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id) 
    comments = Comment.objects.filter(post=post)  
    comment_form = CommentForm()  

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post  
            new_comment.save() 

            return redirect('post_detail', id=post.id)  

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST) 
        if form.is_valid():  
            form.save()  
            return redirect('post_list')  
    else:
        form = BlogPostForm() 

    return render(request, 'create_post.html', {'form': form})




def add_comment(request, id):
    post = get_object_or_404(BlogPost, id=id)  
    if request.method == 'POST':
        form = CommentForm(request.POST)  
        if form.is_valid(): 
        
            comment = form.save(commit=False)
            comment.post = post  
            comment.save() 
            return redirect('post_detail', id=post.id)  
    else:
        form = CommentForm()  

    return render(request, 'add_comment.html', {'form': form, 'post': post})



def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id) 
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()  
            return redirect('post_detail', id=post.id)  
    else:
        form = BlogPostForm(instance=post) 

    return render(request, 'edit_post.html', {'form': form, 'post': post})


def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id) 
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  
        if form.is_valid():
            form.save()  
            return redirect('post_detail', id=comment.post.id)  
    else:
        form = CommentForm(instance=comment)  

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})


def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id) 
    if request.method == 'POST':
        post.delete()  
        return redirect('home')  
    return render(request, 'delete_post_confirm.html', {'post': post})  



def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id) 
    if request.method == 'POST':
        comment.delete()  
        return redirect('post_detail', id=comment.post.id)
    return render(request, 'delete_comment_confirm.html', {'comment': comment})  