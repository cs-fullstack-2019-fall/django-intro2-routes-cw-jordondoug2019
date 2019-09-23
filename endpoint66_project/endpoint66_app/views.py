from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the endpoint66 : type gogetthegood/ or happyhappyjoyjoy/ for more")

def gogetthegood(request):
    return HttpResponse('Here you go! A new pair of vans!')

def happyhappyjoyjoy(request):
    return HttpResponse('Having people that care about you in this life time.')

def youheard(request,words):
    return HttpResponse(words + ' , I heard you!')
