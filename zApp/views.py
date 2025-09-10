from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Question,Choice
from django.http import Http404
from django.shortcuts import  get_object_or_404,render
from django.db.models import F
from django.views import generic
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list}
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

# Ashortcut get_object_or_404()
def detail(request,question_id):
    question = get_object_or_404(Question ,pk=question_id) 
    return render(request,"detail.html",{"question":question})
#get_list_or_404()

#real version
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["CHOICE"])
    except (KeyError,Choice.DoesNotExist):   
        return render(request,"detail.html",{"question":question,"error_message":"You didnt select a choice."},)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results",args=(question_id)))

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"result.html",{"question":question})

#using generic views
class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # same as above, no changes needed.
    ...    