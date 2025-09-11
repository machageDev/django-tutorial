from datetime import datetime, timezone
from django.db import models

# Create your models here.
"""class Question(models.Model):
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


from django.contrib import admin


class Question(models.Model):
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    """
    
    
class MpesaPayment(models.Model):
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mpesa_receipt_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    transaction_date = models.DateTimeField()
    result_code = models.IntegerField()
    result_desc = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} ({self.mpesa_receipt_number})"    