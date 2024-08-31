from django.urls import path
from allauth.socialaccount.views import signup
from authentication.views import GoogleLogin

urlpatterns = [
    path("google/", GoogleLogin.as_view(), name="google_login"),
]