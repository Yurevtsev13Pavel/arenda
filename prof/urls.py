from django.urls import path

import prof
from prof.views import edit_profile, prof_create_view, ProfileUpdateView

app_name = 'prof'
urlpatterns=[
    path('prof/',  edit_profile, name='edit_pro'),
    path('prof_create/', prof_create_view, name='prof_create'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='prof_update'),
]