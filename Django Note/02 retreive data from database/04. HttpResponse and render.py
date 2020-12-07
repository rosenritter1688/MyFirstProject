

#! 2 ways of passing data from the database to template
#* for HttpResponse
#from django.shortcuts import render
from django.http import HttpResponse
from .models import Item  ##load Item table from models.py
from django.template import loader


def helloworld(request):#request from the user
    item_list = Item.objects.all()   
    ## retrieving all objects from table "Item" > item_list
    template = loader.get_template("food/index.html")
    #* tell django where to location the template
    #* MyFirstProject\food\templates\food\index.html
    context ={
        "item_list_pass2template" : item_list,
    }   #name a variable item_list_pass2template for passing data to template
        #pass item_list2 to \MyFirstProject\food\templates\food\index.html
    return HttpResponse(template.render(context,request)) # display item_list

#* for render


def helloworld(request):#request from the user
    item_list = Item.objects.all()   
    ## retrieving all objects from table "Item" > item_list
    context ={
        "item_list_pass2template" : item_list,
    }   #name a variable item_list_pass2template for passing data to template
        #pass item_list2 to \MyFirstProject\food\templates\food\index.html
    return render(request,"food/index.html",context)
                  #pass the request
                           #the location of template
                                            #pass the context
