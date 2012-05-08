import flickrapi
from django.conf import settings
from django.core.cache import cache

# flickr api identifiers
key = settings.FLICKR_KEY
secret = settings.FLICKR_SECRET
user_id = settings.FLICKR_USER_ID

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
