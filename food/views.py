from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#? for retriving data for simplest way
from .models import Item  ##Item table
'''
food/urls.py
urlpatterns = [
    path('hello/', views.helloworld,name='helloworld'),     #in views.py use function helloworld #! 需要告知default urls連到這邊來
    path('item/',views.item,name='item'),
]
'''
#* check urls for 
def helloworld(request):#request from the user
    item_list = Item.objects.all()   ## from Models. Item all objects from table "Item" > item_list
    return HttpResponse(item_list)
def item(request):
     return HttpResponse('This is an item view')
