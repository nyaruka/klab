from .views import *

urlpatterns = ApplicationCRUDL().as_urlpatterns()
urlpatterns += MemberCRUDL().as_urlpatterns()

