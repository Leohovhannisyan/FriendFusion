from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from polls.models import FFUser
from django.shortcuts import redirect
from polls.models import Post
from django.core.mail import send_mail
from django.conf import settings

def profile_info(request):
    user = User.objects.get(username=request.session.get("username"))
    fuser = FFUser.objects.get(user=user)
    email = user.email
    age = fuser.age
    country = fuser.country
    city = fuser.city
    user_image = fuser.profile_image
    context = {"email":email, "email":email,"age": age, "country": country, "city": city,"image":user_image,"username":request.session.get("username")}
    return render(request,'profile.html', context)

def customize_profile(request):
    user_name = request.session.get("username")
    user = User.objects.get(username=user_name)
    fuser = FFUser.objects.get(user=user)
    context = {"image":fuser.profile_image,"user_name" : user_name, "age":fuser.age, "city": fuser.city, "country":fuser.country, "email":user.email}
    return render(request, 'custom_prof.html',context)

def profile_data(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get("username"))
        email = request.POST.get("email")
        age = request.POST.get("age")
        country = request.POST.get("country")
        city = request.POST.get("city")
        profile_image = request.FILES["image"]
        user.email = email
        fuser = FFUser.objects.get(user=user)
        fuser.age = age
        fuser.country = country
        fuser.city = city
        fuser.profile_image = profile_image
        fuser.save()
        user.save()

        return  redirect("main_menu")
    else:
        return HttpResponseBadRequest("Invalid request method")
