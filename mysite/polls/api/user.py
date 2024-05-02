from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import FFUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from polls.group import  Group
from django.contrib.auth import logout
from django.shortcuts import redirect
from polls.models import ApiKey
def register(request):
    if request.method == 'GET':
        return render(request, "register.html")

    else:
        first_name = request.POST["name"]
        last_name = request.POST["surname"]
        username = request.POST["username"]
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        fuser = FFUser(user=user)
        fuser.save()

        import string
        import random

        ApiKey(user=fuser, api_key=''.join(random.choice(string.ascii_lowercase) for i in range(16))).save()

        return render(request,"log_in.html")


def log_in(request):
    if request.method == 'GET':
        return render(request, 'log_in.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            fuser = FFUser.objects.get(user=user, is_removed=False)
            api_key = ApiKey.objects.get(user=fuser)
            request.session['username'] = user.username
            request.session['api_key'] = api_key.api_key
            return redirect('main_menu')

        else:
            return render(request, 'log_in.html', context={'error_message': 'Wrong username or password'})



