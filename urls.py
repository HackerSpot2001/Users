from django.urls import path
from .views import *

urlpatterns = [
    path('logoff', view=logoff, name='Logoff User'),
    path('profile', view=get_profile, name='User Profile'),
    path('login_user', view=login_user, name='Login User'),
    path('create_user', view=create_user, name='Create User'),
]
