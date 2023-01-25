from django.urls import path
from accounts.views import *


urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("signup/", user_signup, name="user_signup"),
]
