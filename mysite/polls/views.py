from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import FFUser, Post
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from .group import  Group

def landing_page(request):
    return render(request, 'landing.html')
def log(request):
    return render(request, 'log_in.html')
def reg(request):
    return render(request, 'register.html')

def redirect_main(request):
    return redirect("main_menu")
def main_menu(request,post_name):
    user_first_name = request.session.get('username')
    user = User.objects.get(username=user_first_name)
    fuser = FFUser.objects.get(user=user)
    user_image = fuser.profile_image
    context = {
        "user_first_name": user_first_name,
        "user_image" : user_image,  
    }
    if post_name:
        post = Post.objects.get(title=post_name)
        topic = post.topic
        image = post.image
        like = post.like
        dislike = post.dislike
        created_at = post.created_at
        context.update({"title" : post_name,
        "topic" : topic,
        "image" : image,
        "like" : like,
        "author": user_first_name, 
        "dislike": dislike,
        "created_at" : created_at})
    return render(request, 'main_menu.html', context)







