from django.db import models
from  .user import FFUser
from .comment import Comment
from django.contrib import admin
class Post(models.Model):
    title = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    image = models.ImageField(default=None)
    author = models.ForeignKey(FFUser, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.ForeignKey(Comment, on_delete = models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "topic", "user", "created_at"]
    def user(self, obj):
        return obj.author.user.username

