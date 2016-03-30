from django.test import TestCase
from smartmin.tests import SmartminTest


class KLabTest(SmartminTest):
    """
    Base unit test class for kLab.. just does some basic housekeeping for us
    like setting up an admin user etc.
    """
    def setUp(self):
        super(KLabTest, self).setUp()

        self.admin = self.create_user('admin', ["Administrator"])
        self.editor = self.create_user('editor', ["Editors"])