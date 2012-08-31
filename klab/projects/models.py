from django.db import models
from members.models import *

class Project(SmartModel):
    title = models.CharField(max_length=64, default="Anonymous Project", help_text='The title of the project')
    description = models.TextField(max_length=2048, help_text="Reviewed description of the project, this will be published on the website")

    owner = models.ForeignKey(Member, help_text="The owner of the project")

    def __unicode__(self):
        return "%s_%s" % (self.owner, self.title)


