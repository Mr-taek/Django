from django.urls import path

from . import views

app_name="polls" # 이유는 모르겠지만, 알아서 namespace를 polls로 설정해버림 ㄷㄷ..

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:question_id>/",views.detail,name="detail"),
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
]