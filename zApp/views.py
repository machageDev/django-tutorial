from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question
from django.http import Http404
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    comtext = {"latest_question_list":latest_question_list}
    return HttpResponse(template.render(context, request))
    
def detail(request,question_id):
    return HttpResponse("You are looking for question %S"% question_id)

def result(request,question_id):
    response = " You are looking at the result of question %s"
    return HttpResponse(response %question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does nor exist")
    return render (request,"detail.html",{"question":question})    