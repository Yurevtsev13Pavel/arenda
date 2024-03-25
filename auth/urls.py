from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

app_name = 'custom_app'

urlpatterns = [
    path('sign-up/', CreateView.as_view(template_name='sign-up.html',
                                        success_url=reverse_lazy('auth:login'),
                                        form_class=UserCreationForm,
                                        model = User), name = 'sign-up'),
    path('sign-in/', LoginView.as_view(template_name = 'sign-in.html'),  name='login')
]