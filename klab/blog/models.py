from django.core.urlresolvers import reverse
from klab import flickr

import json
from django.db import models
from smartmin.models import SmartModel
from django.core.cache import get_cache

class Post(SmartModel):
    """
    Blog post
    """
    TYPE_BLOG = 'B'
    TYPE_STARTUP = 'S'
    POST_TYPES_CHOICES = ((TYPE_BLOG, "Blog"),
                          (TYPE_STARTUP, "Startup"))

    title = models.CharField(max_length=128,
                             help_text="Meaningful one line explenation")
    body = models.TextField(help_text="Detailed content of the post")
    image_id = models.CharField(max_length=128,
                            help_text="The flickr image id tagged blog")

    post_type = models.CharField(default=TYPE_BLOG, max_length=1, choices=POST_TYPES_CHOICES,
                                 help_text="Whether this post is a blog post or a startup")

    def __unicode__(self):
        return self.title

    def get_public_url(self):
        if self.post_type == Post.TYPE_STARTUP:
            return reverse('public_startup', args=[self.pk])
        return reverse('public_post', args=[self.pk])

    def get_cache_key(self):
        return 'flickr_blog_photos_%d' % self.pk

    def photo(self):
        cache = get_cache('default')
        key = self.get_cache_key()

        try:
            if not cache.get(key):
                blog_photos = flickr.api.walk(user_id=flickr.user_id, tags="blog")
                blog_photos_list = list(iter(blog_photos))
                cache.set(key, json.dumps([dict(elt.items()) for elt in blog_photos_list]), timeout=None)

            cached_blog_photos = cache.get(key)
            blog_photos = json.loads(cached_blog_photos)

            for photo in blog_photos:
                if photo.get('id') == self.image_id:
                    return flickr.get_url(photo, "b")

        except:
            pass

    def teaser(self):
        words = self.body.split(" ")

        if len(words) < 100:
            return self.body
        else:
            return " ".join(words[:100]) + " ..."

