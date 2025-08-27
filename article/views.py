from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm


# Create your views here.

def get_all(request):
    articles=Article.objects.all()
    context={
        'articles':articles
    }
    return render(request,'article/home.html',context)

def make_article(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ArticleForm()
    return render(request,'article/make.html',{'form':form})

def get_detail(request,pk):
    articles=Article.objects.get(pk=pk)
    context={
        'articles':articles
    }
    return render(request,'article/detail.html',context)

