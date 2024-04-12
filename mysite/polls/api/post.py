from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import FFUser
from polls.models import Post
def post_menu(request):
    return render(request,"post_menu.html")

def submit_post(request):
   title = request.POST["title"]
   topic = request.POST["topic"]
   image = request.FILES["image"]
   puser = FFUser.objects.get(user=User.objects.get(username=request.session.get("username")))
   post = Post(title=title, topic=topic, image = image, author=puser)
   post.save()
   return render(request, "main_menu.html")

