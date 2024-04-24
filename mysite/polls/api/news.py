from django.shortcuts import render
from polls.models import New
def show_news(request):
    news_list = []
    news = New.objects.filter(author="FriendFusion")
    for new in news:
        news_list.append(new)

    context= {"news_list":news_list}
    return render(request,"news.html",context)
