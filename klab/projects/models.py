from django.db import models
from klab.members.models import *

class Project(SmartModel):
    title = models.CharField(max_length=64, help_text='The title of the project')
    description = models.TextField(max_length=2048, help_text="Reviewed description of the project, this will be published on the website")

    logo = models.ImageField(upload_to="projects/logos", null=True,blank=True, help_text="A logo for your project")
    owner = models.ForeignKey(Member, help_text="The owner of the project")

    def __unicode__(self):
        return "%s_%s" % (self.owner, self.title)


