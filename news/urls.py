from django.urls import path


from news.views import AllObjectView, ObjectDetail

app_name = 'news'
urlpatterns=[
    path('', AllObjectView.as_view(), name='main'),
    path('<int:pk>/', ObjectDetail.as_view(), name='object_detail'),
]