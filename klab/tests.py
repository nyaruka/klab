from smartmin.tests import SmartminTest
from klab.opportunities.models import Opportunity
from klab.events.models import Event
from time import strftime
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase


class KLabTest(SmartminTest):
    """
    Base unit test class for kLab.. just does some basic housekeeping for us
    like setting up an admin user etc.
    """
    def setUp(self):
        super(KLabTest, self).setUp()

        self.admin = self.create_user('admin', ["Administrator"])
        self.editor = self.create_user('editor', ["Editors"])


class Helpers(KLabTest):
    """Helper Class for creating for creating object model on the fly"""
    def setUp(self):
        super(Helpers,self).setUp()

    def create_event(self,day,title,description):
	self.event_date = timezone.now() + timedelta(days=day)
	return Event.objects.create(title=title,
                                    date=self.event_date,
                                    time=strftime('%H:%S'),
                                    duration=60,
                                    description=description,
                                    venue="kLab Telecom House 6th Floor",
                                    logo="photos/35db7336e61cfa7066fb8fbb6308f01b.jpg",
                                    created_by=self.editor,
                                    modified_by=self.editor)

    def create_opportunity(self,days,title,description,link):
        return Opportunity.objects.create(title=title,
                                          description=description,
                                          remaining_days=days,
                                          link=link,
                                          created_by=self.editor,
                                          modified_by=self.editor)
