from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):#request from the user
    return HttpResponse('Hello Wold')

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')
                        #? html code can put in there but its not a proper way to do so