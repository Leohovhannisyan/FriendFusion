from django.shortcuts import render
from polls.models import Group
def show_group_chat(request, group_name):
   member_list = []
   group = Group.objects.get(name=group_name)
   members = group.members.all()
   for member in members:
       member_list.append(member)
   context = {"name":group_name,"member_list":member_list}
   return render(request,"group_chat.html",context)
