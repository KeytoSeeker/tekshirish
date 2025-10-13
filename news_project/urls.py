from django.urls import path
from .views import all_news, detail, home_page_view


urlpatterns = [
    path('all_news/', all_news, name='all_news'),
    path('all_news/<int:pk>/', detail, name='detail'),
    path('', home_page_view, name='home_page'),
]
