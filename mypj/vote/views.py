from django.shortcuts import render,get_object_or_404
from vote.models import LEEKT,Question
# Create your views here.


def detail(request,question_id):
    question=get_object_or_404(LEEKT,pk=question_id)
    return render(request,"vote/leekt.html",{'question':question})

# 한 번도 실수를 해보지 않은 사람은 , 한 번도 새로운 것을 시도한 적이 없는 사람이다

