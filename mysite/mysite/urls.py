"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from polls.api.user import register, log_in, user_log_out
from polls.views  import main_menu, log, reg,redirect_main
from polls.api.profile import profile_info, profile_data, customize_profile
from polls.api.group import group_menu, create_group_view, group_form
from polls.api.post import  post_menu, submit_post
from polls.api.news import show_news
from polls.api.chat import show_group_chat
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/log', log, name='log'),
    path("reg/",reg,name='reg'),
    re_path("main/(?P<post_name>[\w-]*)?",main_menu,name = 'main_menu'),
    path("redirect/", redirect_main, name="redirect_main"),
    path('check/', reg,name="reg"),
    path("register",register, name ='register'),
    path("log_in",log_in,name="log_in"),
    path("user_log_out", user_log_out, name="user_log_out"),
    path("profile/",profile_info, name="profile_info"),
    path("page/", profile_data, name="profile_data"),
    path("group/", group_menu, name="group_menu"),
    path("mainn/", create_group_view, name="create_group_view"),
    path("submitgroup/", group_form, name="group_form"),
    path("add", customize_profile, name="customize_profile"),
    path("post_menu/", post_menu, name="post_menu"),
    path("submit/",submit_post,name='submit_post'),
    path("news/", show_news, name="show_news"),
    path("group_chat/<str:group_name>/", show_group_chat, name="show_group_chat")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
