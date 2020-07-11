from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Lead

class IndexView(generic.ListView):
    template_name = "leads/index.html"
    # context_object_name = "leads"

    def get_queryset(self):
        return Lead.objects.order_by("-created_at")

class LeadCreate(CreateView):
    model = Lead
    fields = ['lead_title','lead_text', 'created_at']

# # def index(request):
# #     leads = Lead.objects.all()
    
# leads = Lead.objects.all()

# for lead in leads:
#     print(lead.lead_title)