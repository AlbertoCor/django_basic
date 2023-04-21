from django.shortcuts import render, get_object_or_404
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
    # question = Question.objects.get(pk=question_id) - Option 1
    question = get_object_or_404(Question, pk= question_id)
    # return HttpResponse(f"You are looking question # {question_id} ")
    return render(request, "poll/detail.html", {
        "question": question
    })

def results(request, question_id):
    return HttpResponse(f"You are looking results from question # {question_id} ")

def vote(request, question_id):
    return HttpResponse(f"You are voting to question # {question_id} ")

