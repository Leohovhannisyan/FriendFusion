from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import FFUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from .group import  Group

def log(request):
    return render(request, 'log_in.html')
def reg(request):
    return render(request, 'register.html')

def main_menu(request):
    user_first_name = request.session.get('username')
    context = {
        "user_first_name": user_first_name,
        
    }
 
    return render(request, 'main_menu.html', context)







