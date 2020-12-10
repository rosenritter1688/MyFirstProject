from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#? for retriving data for simplest way
from .models import Item_frm_model  ##load Item table from models.py
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
#? http://127.0.0.1:8000/item/
def foods(request):#! accept request from the user
    item_list = Item_frm_model.objects.all()   
              #!Item from models
    ## retrieving all objects from table "Item" > item_list
    #template = loader.get_template("food/index.html") #not using coz of using render
    #! line 23 is not needed coz we use render at the line 36,
    #! if wanna use line 23, line 37 is needed and line 33 is not required anymore
    #* tell django where to location the template
    #* MyFirstProject\food\templates\food\index.html
    context ={
        "item_list_frm_views_pass2template" : item_list,
    }   #name a variable item_list_pass2template for passing data to template
        #pass item_list2 to \MyFirstProject\food\templates\food\index.html
    return render(request,"food/index.html",context) #! pass to template food/index.html
                  #pass the request
                           #the location of template
                                            #pass the context
    #return HttpResponse(template.render(context,request)) # display item_list
    #! we can use render instead of using Http HttpResponse
    ##                 
    #! context is set to empty
    #!    context ={
    #!   
    #!
    ##PizzaBurgerBurritofrench fries 
    #* not in readable format
    #* so we shall use TEMPLATE to display 
    #! context is used for passing data from database to template
                       
                       
#? http://127.0.0.1:8000/item-test/
def item(request):
     return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):#accept request
    item = Item_frm_model.objects.get(pk=item_id) #accept item_id <PK> to collect all detail data
    context = {
        'item' : item,
    }
    return render(request,"food/detail.html",context)
    #* now got to food/urls to create PATH of the view
