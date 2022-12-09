from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.

# 1번 코딩순서

class BooksModelView(TemplateView):
    template_name='books/index.html'