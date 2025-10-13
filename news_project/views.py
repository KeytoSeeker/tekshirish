from django.shortcuts import render
from .models import News, Category

def all_news(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request, 'news/all_news.html',context)

def detail(request, pk):
    new = News.objects.get(id=pk)
    context = {
        'new':new
    }
    return render(request, 'news/one.html', context)

def home_page_view(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'news/index.html', context)

