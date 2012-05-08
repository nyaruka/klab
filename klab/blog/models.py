import flickr 

from django.db import models
from smartmin.models import SmartModel

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

    def photo(self):
        for photo in flickr.api.walk(user_id=flickr.user_id, tags="blog"):
            if photo.get('id') == self.image_id:
                return flickr.get_url(photo,"b")

