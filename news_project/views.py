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
    last_news = News.objects.all().order_by("-published_at")[:6]
    uzb_news_last=News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact="o‘zbekiston").order_by("-published_at")[0]
    uzb_news=News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact="o‘zbekiston").order_by("-published_at")[1:5]
    jahon_yangiliklari=News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact="jahon").order_by("-published_at")[0]
    jahon_yangiliklar = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact="jahon").order_by("-published_at")[1:5]
    Iqtisodiyot_last_news=News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact="iqtisodiyot").order_by("-published_at")[0]
    Iqtisod_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="iqtisodiyot").order_by("-published_at")[1:5]
    sport_last = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="sport").order_by("-published_at")[1:5]
    sport_last_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="sport").order_by("-published_at")[0]


    context = {
        'categories': categories,
        'news': news,
        'last_news': last_news,
        'uzb_news_last': uzb_news_last,
        'uzb_news': uzb_news,
        'jahon_yangiliklari':jahon_yangiliklari,
        'jahon_yangiliklar':jahon_yangiliklar,
        'Iqtisodiyot_last_news':Iqtisodiyot_last_news,
        'Iqtisod_news':Iqtisod_news,
        'sport_last_news':sport_last_news,
        'sport_last':sport_last

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



def for_base_html(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories':categories,
        'news':news

    }
    return render(request, 'news/base.html', context)