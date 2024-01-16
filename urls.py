from django.urls import path
from .views import *

urlpatterns = [
    path('logoff', view=logoff, name='Logoff User'),
    path('get_profile', view=get_profile, name='Login User'),
    path('login_user', view=login_user, name='Login User'),
]
