from .models import *
from smartmin.views import *
from django.conf import settings
from django.contrib.auth.models import User, Group
from members.models import *

class ProjectCRUDL(SmartCRUDL):
    model = Project
    actions = ('create', 'read', 'update', 'list',)
    permissions = True

    class Read(SmartReadView):
        fields = ('title', 'owner', 'description','logo')

        def get_title(self, obj):
            return str(obj)

        def get_owner(self, obj):
            return str(obj.owner)

    class List(SmartListView):
        fields = ('title', 'owner', 'description')


   
