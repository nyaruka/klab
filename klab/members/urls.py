from django.conf.urls import include, url
from .views import *

activation = MemberCRUDL().view_for_action('activate').as_view()


urlpatterns = ApplicationCRUDL().as_urlpatterns()
urlpatterns += MemberCRUDL().as_urlpatterns()
urlpatterns += [url(r'^member/activate/(?P<token>\w+)/$', activation, name='url_activation')]
