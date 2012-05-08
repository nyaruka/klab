from django.test import TestCase
from ..tests import KLabTest
from django.core.urlresolvers import reverse

class PostTest(KLabTest):

    def test_permissions(self):
        self.fetch_protected(reverse('blog.post_create'), self.admin)
        self.fetch_protected(reverse('blog.post_create'), self.editor)

