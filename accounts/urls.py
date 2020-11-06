from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    path('profile/', profile_register, name="profile"),
    # path('profile/', profile, name="profile")
]
