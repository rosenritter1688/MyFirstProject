from . import views #     . means current directory     <import views.py>
from django.urls import path


urlpatterns = [
    path('hello/', views.helloworld,name='helloworld'),     #in views.py use function helloworld #! 需要告知default urls連到這邊來
    path('item/',views.item,name='item'),
]
#! #http://127.0.0.1:8000/hello
#! #http://127.0.0.1:8000/item

#! 前面有宣告過告知default urls連到這邊來所以這個就不用打
##django has no obligation to look at this file, django will only look at the urls.py which in in the prokect folder "MyFirstProject"
##C:\Users\Bruce Ashbee\Documents\MyFirstProject\MyFirstProject\urls.py
##

#urlpatterns = [
#    path('', views.helloworld,name='helloworld'),     #in views.py use function helloworld 
#]
#!http://127.0.0.1:8000/
#? 不可以路徑放空的會有page not found的問題!!!，雖然課程有這樣打