from django.contrib import admin
from django.urls import path, reverse
from . import views
from .models import Lead


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.LeadCreate.as_view(), name="create"),
    path('<int:pk>/update/', views.LeadUpdate.as_view(), name="update"),
    path('<int:pk>/delete/', views.LeadDelete.as_view(), name="delete"),
]
