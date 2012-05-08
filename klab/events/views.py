from .models import *
from smartmin.views import *

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

