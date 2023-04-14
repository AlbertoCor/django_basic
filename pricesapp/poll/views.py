from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# view name index, function based view
def index(request):
    lastest_question_list = Question.objects.all()
    # return HttpResponse("You are in main page")
    return render(request, "poll/index.html", {
        "lastest_question_list":lastest_question_list
    })

def detail(request, question_id):
    return HttpResponse(f"You are looking question # {question_id} ")

def results(request, question_id):
    return HttpResponse(f"You are looking results from question # {question_id} ")

def vote(request, question_id):
    return HttpResponse(f"You are voting to question # {question_id} ")

