from django.shortcuts import render,get_object_or_404
from polls.models import Question,Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# 코딩 순서 , 먼저 어떤 기능을 만들지 구상
# urlconf해서 어떤 이름과 내용으로 들어올 지를 구상
# view 함수와 urlconf 연결, e.g : 아 url을 이렇게 넘어갈 거니까 views에 함수는 이렇게 정의할 거고. 
# 그 다음, views에 넘어와서 view함수를 작성하는데, 여기서 접근시킬 Model(DB)를 가져오고 , 이제 이 DB를 templates로 넘겨줄 것임
# templates-> view함수에서 template로 넘기는 변수등을 기억(Model의 주소를 담고 있는 변수라서) , 이제 templates에서 DB에 있는 TABLE을 가져와서 쓸 수 있는것임 (# 단 views가 넘겨준 Table만)
# !중요! views함수에서 render를 하는데, model 데이터베이스 위치를 templates에 넘겨줘서 결국 templates에서 model에 접근할 수 있는 그림임. views가 이걸 할 수 있음



# request는 모든 views함수의 필수 인자
def index(request):
    latest_question_list=Question.objects.all().order_by("-pub_data")[:5] # 이걸 하니까 일단 뭔가 뜸..!
    context={"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={"question":question}
    return render(request,"polls/detail.html",context)

def vote(request, question_id):
    print(question_id)
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        context={
            "question":question,
            "error_message":"you didn't select a choice.",
        }
        return render(request,"polls/detail.html",context)
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results",args=(question.id)))
        # Redirect를 함으로서 결과 페이지를 바로 옮기게 하는 기능을 한다고 함

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})