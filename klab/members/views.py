from .models import *
from smartmin.views import *
from django.conf import settings

class ApplicationCRUDL(SmartCRUDL):
    model = Application
    actions = ('create', 'read', 'update', 'list', 'thanks')
    permissions = True

    class Read(SmartReadView):
        fields = ('professional_status', 'applying_for', 'frequency',
                  'goals', 'education', 'experience')

        def get_name(self, obj):
            return str(obj)

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


