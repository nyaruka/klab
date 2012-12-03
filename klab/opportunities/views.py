from .models import *
from smartmin.views import *

class OpportunityCRUDL(SmartCRUDL):
    model = Opportunity
    actions = ('create', 'update', 'list')

    class List(SmartListView):
        fields = ('title', 'link', 'deadline', 'created_by')

    class Update(SmartUpdateView):
        fields = ('title', 'description', 'remaining_days', 'link')

    
    class Create(SmartCreateView):
        fields = ('title', 'description', 'remaining_days', 'link')
    
