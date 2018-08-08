from .models import *
from smartmin.views import *
from django.core.cache import cache

class EventCRUDL(SmartCRUDL):
    model = Event
    actions = ('create', 'update', 'list')
    permissions = True

    class List(SmartListView):
        fields = ('title', 'date', 'photo_tag')

    class Create(SmartCreateView):
        fields = ('date', 'time', 'duration', 'title', 'logo','description', 'venue', 'photo_tag')

    class Update(SmartUpdateView):
        fields = ('is_active', 'date', 'time', 'duration', 'title', 'logo','description', 'venue', 'photo_tag')

        def post_save(self, obj, *args, **kwargs):
            obj = super(EventCRUDL.Update, self).post_save(obj, *args, **kwargs)
            cache.delete(obj.get_cache_key())
            return obj
            

class VideoCRUDL(SmartCRUDL):
    model = Video
    actions = ('create', 'update', 'list')
    permissions = True

    class Create(SmartCreateView):
        fields = ('name', 'summary', 'description', 'youtube_id')

    class Update(SmartUpdateView):
        fields = ('is_active', 'name', 'summary', 'description', 'youtube_id')

    class List(SmartListView):
        fields = ('name', 'summary')
