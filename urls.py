from django.urls import path
from .views import *

urlpatterns = [
    path('logoff', view=logoff, name='Logoff User'),
    path('profile', view=get_profile, name='User Profile'),
    path('remove', view=remove_account, name='Remove User'),
    path('forgot_password', view=forgot_password, name='Forgot Password'),
    path('change_password', view=change_password, name='Change Password'),
    path('login_user', view=login_user, name='Login User'),
    path('create_user', view=create_user, name='Create User'),
    path('update_user', view=update_user, name='Update User'),
    path('update_profile_pic', view=update_profile_pic, name='Update User Pic'),
    path('create_party_group', view=createPartyGroup, name='createPartyGroup'),
    path('activate/<str:user_login_id>/<str:uaid>', view=activate_acc, name='Activate Account'),
]
