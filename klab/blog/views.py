from .models import *
from smartmin.views import *
from django.core.cache import get_cache

class PostCRUDL(SmartCRUDL):
    model = Post
    actions = ('create', 'update', 'list')
    permissions = True

    class List(SmartListView):
        fields = ('title', 'created_by', 'created_on')

    class Update(SmartUpdateView):
        exclude = ('modified_by',)

        def post_save(self, obj, *args, **kwargs):
            obj = super(PostCRUDL.Update, self).post_save(obj, *args, **kwargs)
            cache = get_cache('default')            
            cache.delete(obj.get_key())
            return obj
