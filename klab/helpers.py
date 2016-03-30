from klab.opportunities.models import Opportunity
from klab.events.models import Event
from time import strftime
from django.utils import timezone
from datetime import timedelta
from tests import KLabTest
from smartmin.tests import SmartminTest   

class Helpers(KLabTest):

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