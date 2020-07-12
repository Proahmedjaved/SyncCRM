from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
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
    fields = ['lead_title','lead_text']
    success_url = reverse_lazy('leads:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LeadCreate, self).form_valid(form)

class LeadUpdate(UpdateView):
    model = Lead
    fields = ['lead_title','lead_text']
    success_url = reverse_lazy('leads:index')
    
class LeadDelete(DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:index')