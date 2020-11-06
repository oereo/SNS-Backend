from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name="main"),
    path('generic/', generic, name="generic"),
    path('mypage/', mypage, name="mypage"),
    path('postpage', postpage, name="postpage")
]
