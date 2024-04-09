from django.urls import path

from main import views


app_name = 'main'

urlpatterns = [
    path('', views.main_home, name='main_home'),
]