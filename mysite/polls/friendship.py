from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from .user import FFUser
class FriendShip(models.Model):
    user_1 = models.ForeignKey(FFUser, on_delete= models.CASCADE,related_name="user_1")
    user_2 = models.ForeignKey(FFUser, on_delete= models.CASCADE, related_name= "user_2")

@admin.register(FriendShip)
class FriendShipAdmin(admin.ModelAdmin):
    list_display = ["user_1",  "user_2"]
