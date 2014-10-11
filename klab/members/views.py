from .models import *
from smartmin.views import *
from django.conf import settings
from django.contrib.auth.models import User, Group
from klab.projects.models import *
import random
import string
from django import forms


class MemberPermsMixin(object):
    """
    Facilitate to give a user the permission on the objects he created
    """
    def get_user(self):
        return self.request.user

    def get_object_created_by(self):
        return self.object.created_by
    
    def has_permission(self, request, *args, **kwargs):
        """
        Figures out if the current user has permissions for this view.
        """
        self.kwargs = kwargs
        self.args = args
        self.request = request
        self.object = self.get_object()
        
        has_perm = request.user.has_perm(self.permission)
        
        if self.get_user().is_superuser:
            return True

        if has_perm:
            return self.get_user().id == self.get_object_created_by().id

        return False


class MemberForm(forms.ModelForm):
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)

    project_title = forms.CharField(max_length=48,label="Project Title", help_text="This is the tile of the project you'll be doing at kLab")

    project_description = forms.CharField(max_length=2048,label='Project Description', help_text='This is the project description to be published on the kLab website', widget=forms.widgets.Textarea())

   
    def save(self, commit=True):

        
        member = super(MemberForm, self).save(commit)
        if member.membership_type == 'G':
            project = Project.objects.create(owner=member,created_by=member.user, modified_by= member.user)
            project.title=self.cleaned_data['project_title']
            project.description=self.cleaned_data['project_description']
            project.save()

            member.projects.add(project)

        new_pass = self.cleaned_data['new_password']
        if new_pass:
            
            member.user.set_password(new_pass)
            member.is_active = True
            member.user.save()
            if(commit):
                
                member.save()
        return member

    class Meta:
        model = Member
        fields = ('is_active','application','user','first_name','last_name','phone','email','picture','country','city','neighborhood','education','experience','projects','token')
            
class ApplicationCRUDL(SmartCRUDL):
    model = Application
    actions = ('create', 'read', 'update', 'list', 'thanks', 'csv')
    permissions = True

    class Read(SmartReadView):
        fields = ('professional_status', 'applying_for', 'frequency',
                  'goals', 'education', 'experience', 'approve')

        def get_approve(self, obj):
            member = Member.objects.filter(application=obj)
            if member:
                return '<a class="btn btn-large btn-success disabled" href="#"> Approved <i class="icon-ok icon-white"></i></a>'
            else:
                 
                return '<a class="btn btn-large posterize" href="%s?application=%d">Approve</a>' % (reverse('members.member_new'), obj.id)


        def get_name(self, obj):
            return str(obj)

        def get_professional_status(self, obj):
            return obj.get_professional_status_display()

        def get_applying_for(self, obj):
            return obj.get_applying_for_display()

        def get_frequency(self, obj):
            return obj.get_frequency_display()

    class Csv(SmartCsvView):
        fields = ('created_on', 'name', 'email', 'phone', 'professional_status', 'applying_for', 'frequency', 'city', 'country', 'goals', 'education', 'experience')

        def derive_queryset(self, **kwargs):
            queryset = super(ApplicationCRUDL.Csv, self).derive_queryset(**kwargs)
            return queryset.filter(is_active=True)

        def get_professional_status(self, obj):
            return obj.get_professional_status_display()

        def get_applying_for(self, obj):
            return obj.get_applying_for_display()

        def get_frequency(self, obj):
            return obj.get_frequency_display()
        
    class List(SmartListView):
        fields = ('name', 'email', 'applying_for', 'city', 'country', 'created_on')
        search_fields = ('first_name__icontains', 'last_name__icontains')
        field_config = { 'applying_for': dict(label="Membership Type") }

        

        def derive_queryset(self, **kwargs):
            queryset = super(ApplicationCRUDL.List, self).derive_queryset(**kwargs)
            return queryset.filter(is_active=True)

        def get_name(self, obj):
            return "%s %s" % (obj.first_name, obj.last_name)

        def get_applying_for(self, obj):
            return obj.get_applying_for_display()

    class Create(SmartCreateView):
        permission = None
        success_url = 'id@members.application_thanks'
        field_config = { 'goals': dict(label="Your goals in 1K"),
                         'education': dict(label="Your education in 1K"),
                         'experience': dict(label="Your experience in 1K") }
        submit_button_name = "Apply for Membership"

        def pre_save(self, obj):
            obj = super(ApplicationCRUDL.Create, self).pre_save(obj)
            anon_user = User.objects.get(id=settings.ANONYMOUS_USER_ID)
            obj.created_by = anon_user
            obj.modified_by = anon_user

            return obj

        def post_save(self, obj):
            obj = super(ApplicationCRUDL.Create, self).post_save(obj)

            anon_user = User.objects.get(id=settings.ANONYMOUS_USER_ID)
            obj.created_by = anon_user
            obj.modified_by = anon_user
            
            # make any applications with the same email inactive
            Application.objects.filter(is_active=True, email=obj.email).exclude(id=obj.id).update(is_active=False)

            return obj

        def form_valid(self, form):
            # is our hidden field displayed?  we are probably a bot, return a 200 request
            if 'message' in self.request.REQUEST and len(self.request.REQUEST['message']) > 0:
                return HttpResponse("Thanks for your application.  You appear to be slightly automated however so we may not actually use it.  If you think you have received this in error, please contact the kLab team.")
            else:
                return super(ApplicationCRUDL.Create, self).form_valid(form)

        def get_context_data(self, **kwargs):
            context = super(ApplicationCRUDL.Create, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context

    class Thanks(SmartReadView):
        permission = None


class MemberCRUDL(SmartCRUDL):
    model = Member
    actions = ('create','read', 'update', 'list','new', 'myprofile', 'activate')
    permissions = True

    class Activate(SmartUpdateView):
        form_class = MemberForm
        
        permission = None
        success_message = "Password saved and account activated successfully, now you can login to the website"
        success_url = "@users.user_login"

        def derive_fields(self):
            if self.object.membership_type == 'B':
                return ('new_password',)
            else:
                return ('new_password','project_title','project_description')


        def get_context_data(self, **kwargs):
            context = super(MemberCRUDL.Activate, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context

        def get_object(self, queryset=None):
            token = self.kwargs.get('token')
            return Member.objects.get(token=token)

    class Myprofile(SmartUpdateView):

        fields = ('first_name','last_name','phone','email','picture','country','city','neighborhood','education','experience')
        def has_permission(self, request, *args, **kwargs):
            
            super(MemberCRUDL.Myprofile,self).has_permission(request, *args, **kwargs)
            return True


        def get_context_data(self, **kwargs):
            context = super(MemberCRUDL.Myprofile, self).get_context_data(**kwargs)
            context['base_template'] = 'smartmin/public_base.html'
            return context

        def get_object(self, queryset=None):
            return Member.objects.get(user=self.request.user)


    class Read(SmartReadView):
        fields = ('application','user','first_name','last_name','phone','membership_type','email','picture','country','city','neighborhood','education','education','experience','projects','token')
        def get_membership_type(self, obj):
            return obj.application.get_applying_for_display()

    class List(SmartListView):
        fields = ('name','email','phone','country','city',)
        field_config = { 'email': dict(label="Email / User") }
        search_fields = ('first_name__icontains', 'last_name__icontains')

        def derive_queryset(self, **kwargs):
            queryset = super(MemberCRUDL.List, self).derive_queryset(**kwargs)
            return queryset.filter(is_active=True)

        def get_name(self, obj):
            return "%s %s" % (obj.first_name, obj.last_name)

        def get_membership_type(self, obj):
            return obj.application.get_applying_for_display()
        
    class New(SmartCreateView):
        fields = ('application',)
        success_url = 'id@members.member_read'
        
        def pre_save(self, obj):
            obj = super(MemberCRUDL.New, self).pre_save(obj)
            userapp = obj.application
            obj.first_name = userapp.first_name
            obj.last_name = userapp.last_name
            obj.phone = userapp.phone
            obj.email = userapp.email
            obj.membership_type = userapp.applying_for
            obj.picture = userapp.picture
            obj.country = userapp.country
            obj.city = userapp.city
            obj.neighborhood = userapp.neighborhood
            obj.education = userapp.education
            obj.experience = userapp.experience
            obj.token = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))

            user = User.objects.create(username=obj.application.email,email=obj.application.email)

            user.email_user("kLab account activation","Your membership to kLab has been approved go to the following link to activate your account \n \n http://klab.rw/members/member/activate/%s/  \n \n After you have activated your account, login using your full email address as username and your password \n \n And  customize what will be published on your kLab website profile by click profile link on the left of members \n \n  This email is generated by the kLab website do not reply to it. " % obj.token,"website@klab.rw")
            group = Group.objects.get(name='Members')
            user.groups.add(group)
            user.first_name = userapp.first_name
            user.last_name = userapp.last_name
            user.email = userapp.email
            user.set_unusable_password()
            user.save()

            obj.user = user
            obj.is_active = False
            obj.save()
            return obj

        def post_save(self, obj):
            obj = super(MemberCRUDL.New, self).post_save(obj)
            obj.update_member_picture()
            obj.save()
            return obj
