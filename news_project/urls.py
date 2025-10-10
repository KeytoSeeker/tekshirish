from django.urls import path
from .views import all_news


urlpatterns = [
    path('all_news/', all_news, name='all_news')
]















