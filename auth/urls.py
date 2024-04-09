from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sitemaps.views import index
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

app_name = 'auth'

urlpatterns = [
    path('sign-up/', CreateView.as_view(template_name='sign-up.html',
                                        success_url=reverse_lazy('auth:login'),
                                        form_class=UserCreationForm,
                                        model = User), name = 'sign-up'),
    path('sign-in/', LoginView.as_view(template_name = 'sign-in.html', next_page=reverse_lazy('prof:prof_create')), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('auth:login')), name='logout')

]