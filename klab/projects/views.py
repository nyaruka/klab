from .models import *
from smartmin.views import *
from django.conf import settings
from django.contrib.auth.models import User, Group
from members.models import *

class ProjectCRUDL(SmartCRUDL):
    model = Project
    actions = ('create', 'read', 'update', 'list','shortlist')
    permissions = True

    class Create(SmartCreateView):
        fields = ('title', 'description', 'logo')

        def pre_save(self, obj):
            obj = super(ProjectCRUDL.Create, self).pre_save(obj)
            obj.owner = self.request.user
            return obj

    class Read(SmartReadView):
        fields = ('title', 'owner', 'description','logo')

        def get_title(self, obj):
            return str(obj)

        def get_owner(self, obj):
            return str(obj.owner)

    class List(SmartListView):
        fields = ('title', 'owner', 'description')


    class Shortlist(SmartListView):
        fields = ('title', 'owner', 'description')

        def derive_queryset(self):
            return Project.objects.filter(owner=request.user)
