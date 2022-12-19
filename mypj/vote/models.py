from django.db import models

# Create your models here.

# 내가 여기서 모델을 추가하면 admin에서 뭔가 추가된다는거지??

# table이름은.. LEEKT
class LEEKT(models.Model):
    nametext=models.CharField(max_length=100)#verbose_name="Building",name="constructure"
    pub_date=models.DateField("data publising")

    def __str__(self) -> str:
        return self.nametext

class voting(models.Model):
    candidate=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.candidate

class Question(models.Model):
    word=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.word