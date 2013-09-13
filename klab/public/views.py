import flickr
from datetime import datetime

from models import *
from blog.models import Post
from events.models import Event
from projects.models import Project
from members.models import Member
from opportunities.models import Opportunity

from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.cache import get_cache
from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q

class EmailForm(forms.Form):
    firstname = forms.CharField(max_length=64)
    lastname = forms.CharField(max_length=64)
    email = forms.EmailField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.widgets.Textarea())

     

def home(request):

    try:
        cache = get_cache('default')
    
        if not cache.get('flickr_main'):
            # from flickr photos get one tagged "main"(should have only one)
            main = flickr.api.walk(user_id=flickr.user_id, tags="main", sort="date-posted-desc")
            cache.set('flickr_main', list(iter(main)), 3600)

        main = cache.get('flickr_main')

        if not cache.get('flickr_favorites'):
            # from flickr get all photo elements tagged "favorite"
            favorites = flickr.api.walk(user_id=flickr.user_id, tags="favorite, -main", sort="date-posted-desc")
            cache.set('flickr_favorites', list(iter(favorites)), 3600)

        favorites = cache.get('flickr_favorites')

        images = []
        sizes = ['496x374', '296x224', '296x146', '194x146', '194x224']

        
        main_photo = main[0]
        images.append((flickr.get_url(main_photo, 'b'), sizes[0], main_photo.get('title')))

        # create an image file from every favorite
        for i,favorite in enumerate(favorites):  
            if main_photo.get('id') != favorite.get('id'):
                images.append((flickr.get_url(favorite, 'b'), sizes[i % len(sizes)], favorite.get('title')))
    except:
        images = []

    # get recent blog posts
    recent = Post.objects.filter(is_active=True).order_by('-created_on')[:5]

    # get upcoming events
    upcoming = Event.objects.filter(is_active=True, date__gte=datetime.today())[:5]

    context = dict(images = images, recent=recent, upcoming=upcoming )
    return render(request, 'public/home.html', context)

def blog(request):
    # get all blog posts in descending order
    posts = Post.objects.filter(is_active=True).order_by('-created_on')

    context = dict(posts=posts)
    return render(request, 'public/blog.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    context = dict(post=post)
    return render(request, 'public/post.html', context)

def projects(request, project_type):
    if project_type == 'all':
        projects = Project.objects.filter(is_active=True).order_by('-created_on')
    else:

        projects = Project.objects.filter(is_active=True).order_by('-created_on')
        
    search = request.REQUEST.get("search",None)
    if search:
        tokens = search.strip().split()
        start_set = projects
        query = Q(pk__lt=0)
        for token in tokens:
            query = query | Q(owner__last_name__icontains=token) | Q(owner__first_name__icontains=token) | Q(title__icontains=token) |  Q(description__icontains=token)
        projects = start_set.filter(query)

    context = dict(projects=projects)
    return render(request, 'public/projects.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    context = dict(project=project)
    return render(request, 'public/project.html', context)
    
def members(request, member_type):

    if member_type == "mentors":
        members = Member.objects.filter(is_active=True,membership_type="B")
    elif member_type == "tenants":
        members = Member.objects.filter(is_active=True,membership_type="G")
    else:
        members = Member.objects.filter(is_active=True).order_by('membership_type')
        
    search = request.REQUEST.get("search",None)
    if search:
        tokens = search.strip().split()
        start_set = members
        query = Q(pk__lt=0)
        for token in tokens:
            query = query | Q(first_name__icontains=token) | Q(last_name__icontains=token)
        members = start_set.filter(query)

    context = dict(members=members,member_type=member_type)
    return render(request, 'public/members.html', context)

def member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    
    
    context = dict(member=member,project=project)
    return render(request, 'public/member.html', context)

def events(request, period):

    if period == "upcoming":
        events = Event.objects.filter(is_active=True, date__gte=datetime.today())
    elif period == "past":
        events = Event.objects.filter(is_active=True, date__lte=datetime.today())
    else:
        events = Event.objects.filter(is_active=True).order_by('-date')

    context = dict(events=events)
    return render(request, 'public/events.html', context)

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    context = dict(event=event)
    return render(request, 'public/event.html', context)

def opportunities(request, status):

    if status == "ending":
        opportunities = Opportunity.objects.filter(is_active=True, deadline__gte=datetime.today())
        group = "Ending Soon"
    elif status == "archived":
        opportunities = Opportunity.objects.filter(is_active=True, deadline__lt=datetime.today())
        group = "Archived"
    else:
        opportunities = Opportunity.objects.filter(is_active=True).order_by('-created_on')
        group = "Newly posted"

    search = request.REQUEST.get("search",None)
    if search:
        tokens = search.strip().split()
        start_set = opportunities
        query = Q(pk__lt=0)
        for token in tokens:
            query = query | Q(title__icontains=token) | Q(link__icontains=token)
        opportunities = start_set.filter(query)


    context = dict(opportunities=opportunities, group=group)
    return render(request, 'public/opportunities.html', context)


def aboutus(request):
    #
    context = {}
    return render(request, 'public/abouts.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['info@klab.rw']
            title = 'kLab Contact us message from %s' % name
            send_mail( title, message + '\n \nFrom ' + name + '\nReply to ' + email,email, recipients)
            return render_to_response('public/contact_success.html',context_instance=RequestContext(request))
    else:
        form = ContactForm()
    return render(request,'public/contact.html',{'form':form,})
