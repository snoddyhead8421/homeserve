from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myelectric/home.html')

def about(request):
    return render(request, 'myelectric/about.html')

def base(request):
    return render(request, 'myelectric/base.html')
