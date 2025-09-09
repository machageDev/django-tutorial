from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date_published")
    def __str__(self):
        return self.question_text

class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    text_choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)  
    def __str__(self):
        return self.text_choice
    