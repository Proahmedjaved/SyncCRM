from leads.api.views import leadList, userLeadList, userList, updateLeadList,createLead
from django.urls import path

urlpatterns = [
    path("", leadList, name="api_leads"),
    path("<int:pk>/create/", createLead, name="api_create_lead"),
    path("users/", userList, name="api_users"),
    path("<int:id>", userLeadList, name="api_leads_user"),
    path("<int:id>/update/", updateLeadList, name="api_leads_update"),
]
