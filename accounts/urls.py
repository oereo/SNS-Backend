from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    # path('oauth/', kakao_callback, name="oauth"),
    path('profile/', profile_register, name="profile")

]
