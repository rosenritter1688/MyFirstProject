from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#? for retriving data for simplest way
from .models import Item  ##load Item table from models.py
#? from models.py under current folder 
#? import Item table

from django.template import loader
'''
food/urls.py
urlpatterns = [
    path('hello/', views.helloworld,name='helloworld'),     #in views.py use function helloworld #! 需要告知default urls連到這邊來
    path('item/',views.item,name='item'),
]
'''
#food/urls.py
#path('hello/', views.helloworld,name='helloworld'),     #in views.py use function helloworld #! 需要告知default urls連到這邊來
#http://127.0.0.1:8000/hello/
def helloworld(request):#request from the user
    item_list = Item.objects.all()   
    ## retrieving all objects from table "Item" > item_list
    template = loader.get_template("food/index.html")
    #* tell django where to location the template
    #* C:\Users\Bruce Ashbee\Documents\MyFirstProject\food\templates\food\index.html
    context ={
        "item_list" : item_list,

    }
    return HttpResponse(template.render(context,request)) # display item_list
    ##                 ##PizzaBurgerBurritofrench fries
                       #* not in readable format
                       #* so we shall use TEMPLATE to display 
#http://127.0.0.1:8000/item/
def item(request):
     return HttpResponse('<h1>This is an item view</h1>')

