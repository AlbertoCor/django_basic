import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # id - automatically django create a id
    question_text = models.CharField(max_length=255)
    pub_date = models.DateField("date published")
    
    # return text when is called
    def __str__(self):
        return self.question_text
    
    # return recently data 14 hours after today comparate 2 timezones
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    
    # return text when is called
    def __str__(self):
        return self.choice_text