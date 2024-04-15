from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from .user import FFUser

class Question(models.Model):
    STATUS = [
            (1, 'Active'),
            (2, 'Pending'),
            (3, 'Finished'),
            (4, 'Removed')]
    owner = models.ForeignKey(FFUser, on_delete=models.CASCADE)   
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=STATUS)
    voters = models.ManyToManyField(FFUser, related_name="voters", null=True)

    def __str__(self):
        return "{} - {}".format(self.question_text, self.get_status_display())

    def to_dict(self):
        return {
            'id': self.id,
            'owner': self.owner.user.username,
            'question': self.question_text,
            'pub_date': str(self.pub_date)[:-6],
            'status': self.get_status_display()
        }

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user_info', 'question_text', 'pub_date', 'status']
    list_filter = ['status']
    filter_horizontal = ['voters']

    def user_info(self, obj):
        return "{} {}".format(obj.owner.user.first_name, obj.owner.user.last_name)
    user_info.short_description = 'User'
