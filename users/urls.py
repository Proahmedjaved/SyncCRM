from django.contrib import admin
from django.urls import path, reverse
from . import views as user_views

app_name = 'users'
urlpatterns = [
    path('signup/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
]
