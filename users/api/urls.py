from users.api.views import registraion_view
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register", registraion_view, name="register_user_api"),
    path("login", obtain_auth_token, name="login_user_api"),
    

]
