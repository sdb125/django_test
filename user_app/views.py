from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('index')
def dev(request):
    return HttpResponse('dev')
def dev2(request):
    return HttpResponse('dev2')