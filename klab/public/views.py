import flickr
from datetime import datetime

from models import *
from blog.models import Post
from events.models import Event
from projects.models import Project
from members.models import Member

from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    firstname = forms.CharField(max_length=64)
    lastname = forms.CharField(max_length=64)
    email = forms.EmailField()

def home(request):

    # from flickr photos get one tagged "main"(should have only one)
    main = flickr.api.walk(user_id=flickr.user_id, tags="main", sort="date-posted-desc")

    # from flickr get all photo elements tagged "favorite"
    favorites = flickr.api.walk(user_id=flickr.user_id, tags="favorite, -main", sort="date-posted-desc")
    
    images = []
    sizes = ['496x374', '296x224', '296x146', '194x146', '194x224']

    try:
        main_photo = list(iter(main))[0]
        images.append((flickr.get_url(main_photo, 'b'), sizes[0], main_photo.get('title')))

        # create an image file from every favorite
        for i,favorite in enumerate(favorites):  
            if main_photo.get('id') != favorite.get('id'):
                images.append((flickr.get_url(favorite, 'b'), sizes[i % len(sizes)], favorite.get('title')))
    except:
        # create an image file from every favorite
        for i,favorite in enumerate(favorites):        
                images.append((flickr.get_url(favorite, 'b'), sizes[i % len(sizes)], favorite.get('title')))


    # get recent blog posts
    recent = Post.objects.filter(is_active=True).order_by('-created_on')[:5]

    # get upcoming events
    upcoming = Event.objects.filter(date__gte=datetime.today())[:5]

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
   
    context = dict(members=members)
    return render(request, 'public/members.html', context)

def member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    
    
    context = dict(member=member,project=project)
    return render(request, 'public/member.html', context)

def events(request, period):

    if period == "upcoming":
        events = Event.objects.filter(date__gte=datetime.today())
    elif period == "past":
        events = Event.objects.filter(date__lte=datetime.today())
    else:
        events = Event.objects.all().order_by('-date')

    context = dict(events=events)
    return render(request, 'public/events.html', context)

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    context = dict(event=event)
    return render(request, 'public/event.html', context)

def aboutus(request):
    #
    context = {}
    return render(request, 'public/abouts.html', context)
