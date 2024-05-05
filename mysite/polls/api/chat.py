from django.shortcuts import render
from polls.models import Group
from polls.models import FriendShip
from django.contrib.auth.models import User
from polls.models import FFUser
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def show_group_chat(request, group_name):
   member_list = []
   group = Group.objects.get(name=group_name)
   members = group.members.all()
   for member in members:
       member_list.append(member)
   context = {"name":group_name,"member_list":member_list}
   return render(request,"group_chat.html",context)

def show_friend_chats(request):
    username = request.session.get("username")
    user = User.objects.get(username=username)
    fuser = FFUser.objects.get(user=user)
    friends =  FriendShip.objects.filter(user_1=fuser).all()
    return render(request,'friend_chats.html', {'friends': friends})


def friend_room(request,room_id):
    context = {"room_id": room_id,}
    return render(request, "friend_room.html",context)
