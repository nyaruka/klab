from django.conf.urls import patterns, include, url
from .views import *

activation = MemberCRUDL().view_for_action('activate').as_view()


urlpatterns = ApplicationCRUDL().as_urlpatterns()
urlpatterns += MemberCRUDL().as_urlpatterns()
urlpatterns += patterns('/^members/', url(r'activate/(?P<token>\w+)/$', activation, name='url_activation'),)
