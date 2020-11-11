from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name="main"),
    path('generic/', generic, name="generic"),
    path('mypage/', mypage, name="mypage"),
    path('postpage/<int:blog_id>', postpage, name="postpage"),
    path('create/', create, name="create"),
    path('map/', mappage, name="map")
]
