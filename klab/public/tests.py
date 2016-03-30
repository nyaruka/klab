import string
from random import choice
from klab.helpers import Helpers
from klab.events.models import Event
from klab.blog.models import Post
from klab.members.models import Application,Member
from klab.projects.models import Project
from klab.opportunities.models import Opportunity
from django.core.urlresolvers import reverse

class KLabPublicTest(Helpers):

	"""Basic unit test for kLab public website"""
	def setUp(self):
		super(KLabPublicTest, self).setUp()

		self.users = self.create_user('member',["Members"])
		self.post = Post.objects.create(title="Apply for Global Entrepreneurship Summit",
										body="Join Entrepreneurs from all around the world",
										image_id="20919667939",
										created_by=self.editor,
										modified_by=self.editor)
		self.application = Application.objects.create(first_name="John",
                                                       last_name="Boy",
                                                       phone="0786325897",
                                                       email="john.boy@gmail.com",
                                                       picture="members/application/bc16e45b85d30f0d046a20f11821da2b.jpg",
                                                       country="Rwanda",
                                                       city="Kigali",
                                                       neighborhood="Nyarutarama",
                                                       professional_status="EIT",
                                                       applying_for="B",
                                                       frequency="W",
                                                       goals="I'd like to help the next generation young ICT Entrepereneur",
                                                       education="I have a PHD degree in NLP and I've been doing my research in Information Retrieval",
                                                       experience="I've work for several company such as Microsoft,Google and Second Spectrum",
                                                       created_by=self.users,
                                                       modified_by=self.users)
		self.member = Member.objects.create(application=self.application,
                                             user=self.users,
                                             first_name="John",
                                             last_name="Boy",
                                             phone="0786325897",
                                             membership_type="B",
                                             email="john.boy@gmail.com",
                                             picture="members/application/bc16e45b85d30f0d046a20f11821da2b.jpg",
                                             country="Rwanda",
                                             city="Kigali",
                                             neighborhood="Nyarutarama",
                                             education="I have a PHD degree in NLP and I've been doing my research in Information Retrieval",
                                             experience="I've work for several company such as Microsoft,Google and Second Spectrum",
                                             token="".join(choice(string.letters+string.digits) for x in range(32)),
                                             is_alumni=False,
                                             created_by=self.users,
                                             modified_by=self.users)

		self.project = Project.objects.create(title="web application developp",
                                              description="For this project, i will try to fight for the most common problem customers met with the Web Developers from outdated appearance design where i will be doing the better one which can attract every customer to join my service",
                                              owner=self.member,
                                              created_by=self.users,
                                              modified_by=self.users)

	def test_main_page_with_post_past_event(self):
		self.create_event(-1,"$500k Investment Lessons From Seedstars World 2016","This Thursday meet Louis Antoine Muhire, CEO& Founder of Mergims, who is going to clear;y highlight and broadly describe the $500k Investment lessons From Seedstars World 2016.")
		response = self.client.get(reverse('public_home'))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['recent'],
            ['<Post: Apply for Global Entrepreneurship Summit>'])
		self.assertQuerysetEqual(response.context['upcoming'],[])

	def test_main_page_with_post_event(self):
		self.create_event(0,"Demo Night by Skyline Digital","This Wednesday,kLab based startup Skyline Digital that is to officially launch 2 platforms,namely rwandait.rw, which will be covering all IT news in Rwanda")
		response = self.client.get(reverse('public_home'))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['recent'],
    		['<Post: Apply for Global Entrepreneurship Summit>'])
		self.assertQuerysetEqual(response.context['upcoming'],
            ['<Event: Demo Night by Skyline Digital>'])

	def test_event_detail(self):
		event = self.create_event(1,"kLab MTN Day","kLab is hosting the kLab MTN day after so many startup developers and entrepreneurs claiming to not work closely with Rwanda Telecom Companies.")
		response = self.client.get(reverse('solo_event',args=(event.id,)))
		self.assertContains(response,event.title,status_code=200)

	def test_post_detail(self):
		response = self.client.get(reverse('public_post',args=(self.post.id,)))
		self.assertContains(response,self.post.title,status_code=200)

	def test_opportunity_detail(self):
		opportunity = self.create_opportunity(10,"ITU Young Innovators Conflict Challenge","kLab just wants to let you know that the ITU Telecom World 2015 Young Innovators Conflict Challenge is live.","http://ideas.itu.int")
		response = self.client.get(reverse('solo_opportunity',args=(opportunity.id,)))
		self.assertContains(response,opportunity.title,status_code=200)

	def test_members(self):
		response = self.client.get(reverse('public_members',args=("all",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['members'],['<Member: John_Boy>'])

	def test_member_detail(self):
		first_last_name = self.member.first_name + " "+self.member.last_name
		response = self.client.get(reverse('public_profile',args=(self.member.id,)))
		self.assertContains(response,first_last_name,status_code=200)

	def test_projects(self):
		response = self.client.get(reverse('public_projects',args=("all",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['projects'],['<Project: John_Boy_web application developp>'])

	def test_project_detail(self):
		response = self.client.get(reverse('solo_project',args=(self.project.id,)))
		self.assertContains(response,self.project.title,status_code=200)

	def test_events_all(self):
		past_event = self.create_event(-1,"$500k Investment Lessons From Seedstars World 2016","This Thursday meet Louis Antoine Muhire, CEO& Founder of Mergims, who is going to clear;y highlight and broadly describe the $500k Investment lessons From Seedstars World 2016.")
		future_event = self.create_event(1,"kLab MTN Day","kLab is hosting the kLab MTN day after so many startup developers and entrepreneurs claiming to not work closely with Rwanda Telecom Companies.")
		response = self.client.get(reverse('public_events',args=("all",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['events'],['<Event: kLab MTN Day>','<Event: $500k Investment Lessons From Seedstars World 2016>'])

	def test_events_past(self):
		past_event = self.create_event(-1,"$500k Investment Lessons From Seedstars World 2016","This Thursday meet Louis Antoine Muhire, CEO& Founder of Mergims, who is going to clear;y highlight and broadly describe the $500k Investment lessons From Seedstars World 2016.")
		response = self.client.get(reverse('public_events',args=("past",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['events'],['<Event: $500k Investment Lessons From Seedstars World 2016>'])

	def test_events_future(self):
		future_event = self.create_event(1,"kLab MTN Day","kLab is hosting the kLab MTN day after so many startup developers and entrepreneurs claiming to not work closely with Rwanda Telecom Companies.")
		response = self.client.get(reverse('public_events',args=("upcoming",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['events'],['<Event: kLab MTN Day>'])

	def test_posts(self):
		response = self.client.get(reverse('public_blog'))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['posts'],['<Post: Apply for Global Entrepreneurship Summit>'])

	def test_opportunities_new(self):
		new_opportunity = self.create_opportunity(10,"Intellecap: Call for applications for I3N August Investor Showcase","The Intellecap Impact Investment Network (I3N) is now accepting applications from promising impact enterprises for its upcoming Investor Showcase in August 2015 in Nairobi (Date and Venue TBC).","http://ideas.itu.int")
		archived_opportunity = self.create_opportunity(0,"Apps for African City Life","Do you have a suggestion on how mobile technology can support City Life and drive innovation for the Networked Society in Africa?","http://www.ericssonapplicationawards.com/apps-african-city-life")
		response = self.client.get(reverse('public_opportunities',args=("new",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['opportunities'],['<Opportunity: Opportunity object>','<Opportunity: Opportunity object>'])

	def test_opportunities_ending(self):
		new_opportunity = self.create_opportunity(5,"Intellecap: Call for applications for I3N August Investor Showcase","The Intellecap Impact Investment Network (I3N) is now accepting applications from promising impact enterprises for its upcoming Investor Showcase in August 2015 in Nairobi (Date and Venue TBC).","http://ideas.itu.int")
		response = self.client.get(reverse('public_opportunities',args=("ending",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['opportunities'],['<Opportunity: Opportunity object>'])

	def test_opportunities_archived(self):
		archived_opportunity = self.create_opportunity(0,"Apps for African City Life","Do you have a suggestion on how mobile technology can support City Life and drive innovation for the Networked Society in Africa?","http://www.ericssonapplicationawards.com/apps-african-city-life")
		response = self.client.get(reverse('public_opportunities',args=("archived",)))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['opportunities'],[])