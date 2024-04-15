from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from .user import FFUser


class Comment(models.Model):
    user = models.ForeignKey(FFUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def user_info(self,obj):
        return "{}".format(obj.user.username)

