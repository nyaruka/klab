from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('public.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^content/', include('django_quickblocks.urls')),
    url(r'^users/', include('smartmin.users.urls')),
    url(r'^admin/', include(admin.site.urls))
)

# does this environment for development
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
   urlpatterns += patterns('',
       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT,
       }),
   )

def handler500(request):
    """
    500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html') # You need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


