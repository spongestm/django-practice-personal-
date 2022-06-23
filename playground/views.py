from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def empty_response(request):
    return HttpResponse('Auf wiedersien')
def say_hello(request):
    return render(request,'hello.html')
