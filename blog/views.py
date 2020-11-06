from django.shortcuts import render, redirect
from accounts.models import Profile
from .models import Blog
from django.utils import timezone


def main(request):
    return render(request, "index.html")


def generic(request):
    return render(request, 'generic.html')


def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    print(profile)
    return render(request, 'mypage.html')


def postpage(request):
    return render(request, 'postpage.html')


def create(request):
    user = request.user
    blog = Blog()
    blog.user_id = user.id
    blog.owner = user.email
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.image = request.POST['image']
    blog.save()
    # return redirect('/blog/'+str(blog.id))
    return redirect('main')
