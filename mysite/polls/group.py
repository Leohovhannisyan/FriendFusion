from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from .user import FFUser
from django.contrib.auth.models import Permission

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(FFUser, related_name='groups',blank=True)
    admins = models.ManyToManyField(FFUser, related_name='admin_of_groups',blank=True)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]
