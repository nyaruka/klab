from .models import *
from smartmin.views import *
from django.conf import settings
from django.contrib.auth.models import User, Group
from klab.members.models import *
from klab.members.views import MemberPermsMixin

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

        def get_context_data(self, **kwargs):
            context = super(ProjectCRUDL.Create, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context

    class Read(MemberPermsMixin, SmartReadView):
        fields = ('title', 'owner', 'description','logo')

        def get_title(self, obj):
            return str(obj)

        def get_owner(self, obj):
            return "%s %s" % (obj.owner.first_name, obj.owner.last_name)

        def get_context_data(self, **kwargs):
            context = super(ProjectCRUDL.Read, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context


    class List(SmartListView):
        fields = ('title', 'owner', 'description')

        def get_owner(self, obj):
            return "%s %s" % (obj.owner.first_name, obj.owner.last_name)

    class Update(MemberPermsMixin, SmartUpdateView):
        fields = ('title', 'description')
        success_url = "id@solo_project"
        def get_context_data(self, **kwargs):
            context = super(ProjectCRUDL.Update, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context

    class Shortlist(SmartListView):
        fields = ('title', 'owner', 'description')
        add_button = True

        def get_owner(self, obj):
            return "%s %s" % (obj.owner.first_name, obj.owner.last_name)

        def derive_queryset(self):
            member = Member.objects.get(user=self.request.user)
            return Project.objects.filter(owner=member)

        def get_context_data(self, **kwargs):
            context = super(ProjectCRUDL.Shortlist, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context
