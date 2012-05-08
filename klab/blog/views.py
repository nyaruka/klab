from .models import *
from smartmin.views import *

class PostCRUDL(SmartCRUDL):
    model = Post
    actions = ('create', 'update', 'list')
    permissions = True

    class List(SmartListView):
        fields = ('title', 'created_by', 'created_on')

    class Update(SmartUpdateView):
        exclude = ('modified_by',)
