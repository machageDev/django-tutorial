from django.http import HttpResponse
from django.shortcuts import render

from zApp.models import Question

# Create your views here.
def index(request):
     latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("You are looking for question %S"% question_id)

def result(request,question_id):
    response = " You are looking at the result of question %s"
    return HttpResponse(response %question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)