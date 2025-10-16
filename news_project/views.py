from django.shortcuts import render
from .models import News, Category
from .forms import ContactForm
from django.http import HttpResponse
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

def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("xabar adminga yuborildi ✔ <a href=''>Asosiy sahifa </a>")
    context = {
        'form':form
    }
    return render(request, 'news/contact.html',context)
    
def about_view(request):
    context = {}
    return render(request, 'news/about.html',context)

