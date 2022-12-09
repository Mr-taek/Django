from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField('Author') # 아 .. 이것만 쓰면 오류가 나던이유가 뭐냐면.. author이라는 클래스가 필요해서 그럼!
    publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE)
    publication_date=models.DateField()
    def __str__(self) -> str:
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=50)
    salutation=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self) -> str:
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    website=models.URLField()
    def __str__(self) -> str:
        return self.name
# 