from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import FFUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from polls.models import Group
def group_menu(request):
    return render(request, "group_menu.html")

def group_form(request):
    return render(request,"group_form.html")
def create_group_view(request):
    if request.method == "POST":
        name = request.POST["group_name"]
        admin_name = request.session.get("username") 
        user = User.objects.get(username=admin_name)
        admin = FFUser.objects.get(user=user)
        group = Group.objects.create(name=name)
        group.admins.add(admin)
        group.members.add(admin)
        group.save()

        return redirect("main_menu")

    return render(request, 'group_form.html')
