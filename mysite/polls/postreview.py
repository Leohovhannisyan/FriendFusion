from django.db import models
from  .user import FFUser
from .models import Post
from django.contrib import admin
class PostReview(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(FFUser, on_delete=models.CASCADE)
    like = models.BooleanField()



@admin.register(PostReview)
class PostReviewAdmin(admin.ModelAdmin):
    list_display = ["post"]
