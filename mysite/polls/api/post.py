from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import FFUser
from polls.models import Post
from django.shortcuts import redirect

def post_menu(request):
    return render(request,"post_menu.html")

def submit_post(request):
   title = request.POST["title"]
   topic = request.POST["topic"]
   image = request.FILES["image"]
   author_name = request.session.get("username")
   puser = FFUser.objects.get(user=User.objects.get(username=author_name))
   post = Post(title=title, topic=topic, image = image, author=puser)
   post.save()
   return redirect("main_menu",post_name=title) 

