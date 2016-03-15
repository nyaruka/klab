from django.test import TestCase
from smartmin.tests import SmartminTest
from klab.events.models import Event
from klab.blog.models import Post
from django.core.urlresolvers import reverse

class KLabTest(SmartminTest):
    """
    Base unit test class for kLab.. just does some basic housekeeping for us
    like setting up an admin user etc.
    """
    def setUp(self):
        super(KLabTest, self).setUp()

        self.admin = self.create_user('admin', ["Administrator"])
        self.editor = self.create_user('editor', ["Editors"])
        self.post = Post.objects.create(title="Apply for Global Entrepreneurship Summit",
        								body="Join Entrepreneurs from all around the world",
        								image_id="20919667939",
        								created_by = self.editor,
        								modified_by=self.editor)
        self.event = Event.objects.create(title="",
        									date="",
        									time="",
        									duration="",
        									description="",
        									venue="",
        									logo="",
        									description="",
        									recurrence_type="",
        									end_date="",
        									photo_tag="",
        									created_by=self.editor,
        									modified_by=self.editor)

    def test_main_page_with_post_event(self):
    	response = self.client.get(reverse('public_home'))
    	self.assertEqual(response.status_code,200)
    	self.assertQuerysetEqual(response.context['recent'],
    		['<Post: Apply for Global Entrepreneurship Summit>'])
        

