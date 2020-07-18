from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("Hello shop")

def contact(request):
    return HttpResponse("Hello shop")

def tracker(request):
    return HttpResponse("Hello shop")

def search(request):
    return HttpResponse("Hello shop")

def prodView(request):
    return HttpResponse("Hello shop")

def checkout(request):
    return HttpResponse("Hello shop")

