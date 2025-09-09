from datetime import datetime, timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date_published")
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    text_choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)  
    def __str__(self):
        return self.text_choice
    