from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question,Choice
# Create your views here.

def index(request): # callback 함수들 , HttpRequest 객체가 인자로 들옴
    latest_question_list=Question.objects.all().order_by("-pub_date")[:5]
    context={"latest_question_list": latest_question_list}
    return render(request,"polls/index.html",context) # http response 담당 render

def detail(request,question_id): # callback함수 , HttpRequest객체 , polls/<int:question_id> 에서 <int:~>가 추출되어 두개가 들어오ㅓㅁ
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})


def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNot.Exist):
        return render(request,'polls/detail.html',{
            'question':question,
            "error_message":"You didn't select a choice",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})