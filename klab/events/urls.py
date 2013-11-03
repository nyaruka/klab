from .views import EventCRUDL, VideoCRUDL

urlpatterns = EventCRUDL().as_urlpatterns()
urlpatterns += VideoCRUDL().as_urlpatterns()
