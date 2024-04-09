from django.urls import path

import prof
from prof.views import edit_profile
app_name = 'prof'
urlpatterns=[
    path('prof/',  edit_profile, name='edit_pro'),
]