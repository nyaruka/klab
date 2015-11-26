from klab import flickr

from django.db import models
from smartmin.models import SmartModel
from django.core.cache import get_cache

class Post(SmartModel):
    """
    Blog post
    """
    title = models.CharField(max_length=128,
                             help_text="Meaningful one line explenation")
    body = models.TextField(help_text="Detailed content of the post")
    image_id = models.CharField(max_length=128,
                            help_text="The flickr image id tagged blog")    

    def __unicode__(self):
        return self.title

    def get_cache_key(self):
        return 'flickr_blog_photos_%d' % self.pk

    def photo(self):
        cache = get_cache('default')
        key = self.get_cache_key()

        if not cache.get(key):
            blog_photos = flickr.api.walk(user_id=flickr.user_id, tags="blog")
            cache.set(key, list(iter(blog_photos)), 3600)
            
        blog_photos = cache.get(key)

        for photo in blog_photos:
            if photo.get('id') == self.image_id:
                return flickr.get_url(photo,"b")

    def teaser(self):
        words = self.body.split(" ")

        if len(words) < 100:
            return self.body
        else:
            return " ".join(words[:100]) + " ..."

