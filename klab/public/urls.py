from .views import home, blog, post, events, event, aboutus, projects,members,member, project, contact, opportunities

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', home, name='public_home'),
    url(r'^public/blog$', blog, name='public_blog'),
    url(r'^public/blog/post/(\d+)$', post, name='public_post'),
    url(r'public/events/(\w+)$', events, name='public_events'),
    url(r'public/opportunity/(\w*)$', opportunities , name='public_opportunities'),
    url(r'public/projects/(\w+)$', projects, name='public_projects'),
    url(r'public/project/(\d+)$', project, name='solo_project'),
    url(r'public/members/(\w+)$', members, name='public_members'),
    url(r'public/member/(\d+)$', member, name='public_profile'),
    url(r'public/event/(\d+)$', event, name='solo_event'),
    url(r'^public/about$', aboutus, name='public_about'),
    url(r'^public/contact$', contact, name='public_contact'),
)
