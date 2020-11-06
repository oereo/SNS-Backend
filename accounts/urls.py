from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    path('signup/', profile_register, name="signup"),
    path('profile/', profile, name="profile")
]
