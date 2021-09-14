from django.shortcuts import render
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from django.contrib.auth.models import User
@csrf_protect
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def test(request):
    return render(request, 'user/profile.html')

def error_404(request, exception):
    data = {}
    return render(request, 'main/404.html', data)
def error_403(request, exception):
    data = {}
    return render(request, 'main/page-403.html', data)
def error_400(request, exception):
    data = {}
    return render(request, 'main/404.html', data)
def error_500(request, *args, **argv):
    data = {}
    return render(request, 'main/page-500.html', data)

