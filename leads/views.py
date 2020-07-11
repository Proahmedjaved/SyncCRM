from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Lead

class IndexView(generic.ListView):
    template_name = "leads/index.html"
    # context_object_name = "leads"

    def get_queryset(self):
        return Lead.objects.all()

# # def index(request):
# #     leads = Lead.objects.all()
    
# leads = Lead.objects.all()

# for lead in leads:
#     print(lead.lead_title)