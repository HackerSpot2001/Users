from django.urls import path
from .views import *

urlpatterns = [
    # path('login_user', view=login_user, name='Login User'),
    path('logoff', view=logoff, name='Logoff User'),
]
