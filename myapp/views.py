from django.shortcuts import render, redirect
from myapp.models import Article


def article_list(request):
     article = Article.objects.all()
     return render(request, 'article_list.html', {'article': article})



def article_detail(request, pk):
     article = Article.objects.get(pk=pk)
     return render(request, 'article_detail.html', {'article': article})