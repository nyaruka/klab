import json
from django_quickblocks.models import QuickBlock
import flickrapi
from django.conf import settings
from django.core.cache import cache


flickr_block = QuickBlock.objects.filter(quickblock_type__slug='klab_system', title="Flickr").first()
flickr_auth = json.loads(flickr_block.content)

# flickr api identifiers
key = flickr_auth.get('FLICKR_KEY', '1d3206d8ecc5cd053f071a19acf3bbfd')
secret = flickr_auth.get('FLICKR_SECRET', '36149060106ca80e')
user_id = flickr_auth.get('FLICKR_USER_ID', '77982146@N08')

# create flickrapi instance
api = flickrapi.FlickrAPI(key, secret, format='etree', cache=True)

# plugin django cache as flickr cache
api.cache = cache

def get_url(photo,size=None):
    """
    get the url from flickr for a given size (square, thumbnail, small, 640, large)
    """
    farm = photo.get('farm')
    server = photo.get('server')
    photo_id = photo.get('id')
    secret = photo.get('secret')

    if size is None:
        # get the url for medium
        return "http://farm%s.staticflickr.com/%s/%s_%s.jpg" % (farm, server, photo_id, secret)

    return "http://farm%s.staticflickr.com/%s/%s_%s_%s.jpg" % (farm, server, photo_id, secret, size)
