from django.shortcuts import render
from polls.models import FFUser
from polls.models import FriendShip
from django.contrib.auth.models import User
from django.shortcuts import redirect

def add_friend(request):
    if request.method =="POST":
       user = FFUser.objects.get(user=User.objects.get(username=request.session.get("username")))
       future_friend = FFUser.objects.get(user=User.objects.get(username=request.POST["potential_friend"]))
       friendship = FriendShip(user_1=user,user_2=future_friend)
       friendship.save()
       return redirect("main_menu")
