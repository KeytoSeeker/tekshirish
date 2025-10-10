from django.shortcuts import render
from .models import News, Category

def all_news(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request, 'news/all_news.html',context)
