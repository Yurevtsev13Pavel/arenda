from django.urls import path

from news.views import new
app_name = 'news'
urlpatterns=[
    path('', new, name='main'),
]