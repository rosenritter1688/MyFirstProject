from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(request):#request from the user
    return HttpResponse('Hello Wold')
