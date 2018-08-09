from .models import *
from smartmin.views import *
from django.core.cache import cache

class PostCRUDL(SmartCRUDL):
    model = Post
    actions = ('create', 'update', 'list')
    permissions = True

    class List(SmartListView):
        fields = ('title', 'post_type', 'created_by', 'created_on')

        def get_post_type(self, obj):
            return obj.get_post_type_display()

    class Update(SmartUpdateView):
        exclude = ('modified_by',)

        def post_save(self, obj, *args, **kwargs):
            obj = super(PostCRUDL.Update, self).post_save(obj, *args, **kwargs)
            cache.delete(obj.get_cache_key())
            return obj
