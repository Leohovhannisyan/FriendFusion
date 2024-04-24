from django.db import models
from  .user import FFUser

from django.contrib import admin
class New(models.Model):
    title = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    author = models.CharField(default="FriendFusion", max_length = 20)
    image = models.ImageField(default=None)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ["title", "topic", "created_at"]
    def user(self, obj):
        return obj.author.user.username
