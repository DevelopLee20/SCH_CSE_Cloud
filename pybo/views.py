from django.http import HttpResponse
from .models import Question
from django.shortcuts import render

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}

    return render(request, 'pybo/test.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question':question}

    return render(request, 'pybo/question_detail.html', context)