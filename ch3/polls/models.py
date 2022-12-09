from django.db import models

# Create your models here.
# models은 DB와 관련된 사항임..

class Question(models.Model):
    question_text=models.CharField(name="Hi",max_length=200)
    pub_data=models.DateTimeField("date published")
    
    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
