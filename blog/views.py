from django.shortcuts import render
from accounts.models import Profile


def main(request):
    return render(request, "index.html")


def generic(request):
    return render(request, 'generic.html')


def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    print(profile)
    return render(request, 'mypage.html')
