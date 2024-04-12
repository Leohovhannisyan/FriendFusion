from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from polls.models import FFUser
from django.shortcuts import redirect
from polls.models import Post
def profile_info(request):
    user = User.objects.get(username=request.session.get("username"))
    fuser = FFUser.objects.get(user=user)
    email = user.email
    age = fuser.age
    country = fuser.country
    city = fuser.city
    context = {"email":email, "age": age, "country": country, "city": city}
    return render(request,'profile.html', context=context)

def customize_profile(request):
    return render(request, 'custom_prof.html')

def profile_data(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get("username"))
        email = request.POST.get("email")
        age = request.POST.get("age")
        country = request.POST.get("country")
        city = request.POST.get("city")
        profile__image = request.FILES["image"]

        if email and age and country and city != "":
            user.email = email
            fuser = FFUser.objects.get(user=user)
            fuser.age = age
            fuser.country = country
            fuser.city = city
            fuser.profile__image = profile__image
            fuser.save()
            user.save()
            


            return render(request, "main_menu.html")
        else:
            return HttpResponseBadRequest("Enter all data")
    else:
        return HttpResponseBadRequest("Invalid request method")
