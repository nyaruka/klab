from .models import *
from smartmin.views import *
from django.core.cache import get_cache

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
            cache = get_cache('default')            
            cache.delete(obj.get_cache_key())
            return obj
            
