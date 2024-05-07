from django.shortcuts import render
from polls.models import FFUser


def search_users(request):
    if request.method == "POST":
        search_text = request.POST["query"]
        if search_text:
            search_results = FFUser.objects.filter(user__username__icontains=search_text)
            context = {"searched_names":search_results}
            return render(request, "searched_users.html", context)
        else:
            return render(request, "main_menu.html")




