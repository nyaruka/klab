from django.contrib.auth.models import User, Group
from django import forms
from smartmin.views import *
from smartmin.users.views import *

class UserCRUDL(UserCRUDL):
     actions = ('create','update','list', 'activate')

     class Activate(SmartUpdateView):
         form_class = UserForm
         permission = None
         success_message = "Member Activated Successfully."
         success_url = "@users.user_login"
         fields =('new_password',)

         field_config = {
          'new_password': dict(help="Set the user's initial password here."),
        }
