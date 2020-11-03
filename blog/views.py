from django.shortcuts import render


def main(request):
    return render(request, "index.html")


def generic(request):
    return render(request, 'generic.html')
