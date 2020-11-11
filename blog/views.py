from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from .models import Blog
from django.utils import timezone


def main(request):
    user = request.user
    blogs = Blog.objects.all()
    return render(request, "index.html", {'blogs': blogs})


def generic(request):
    return render(request, 'generic.html')


def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    print(profile)
    return render(request, 'mypage.html')


def postpage(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    blog_detail.increaseViews()
    return render(request, 'postpage.html', {'blog_detail': blog_detail})


def mappage(request):
    return render(request, 'map.html')


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
    return redirect('main')
