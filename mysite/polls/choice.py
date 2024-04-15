from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from .user import FFUser
from .question import Question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {} - {}".format(self.question.question_text, self.text, self.votes)

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question.question_text,
            'text': self.text,
            'votes': self.votes
        }

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question_info', 'text', 'votes']

    def question_info(self, obj):
        return obj.question.question_text
    question_info.short_description = 'Question'
