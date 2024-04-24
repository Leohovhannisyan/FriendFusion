from django.contrib import admin
from django.db import models

class Quiz(models.Model):
    answer1 = models.CharField(max_length=120)
    answer2 = models.CharField(max_length=120)
    answer3 = models.CharField(max_length=120)
    answer4 = models.CharField(max_length=120)
    correct_answer = models.IntegerField(default=None)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["id"]
