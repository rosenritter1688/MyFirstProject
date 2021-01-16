from . import views #     . means current directory     <import views.py>
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#*Namespacing
#* in case of your co-workers name their URLs as same asa your
#* in this project we named 3 url page as item, show, detail
#* even other ppl name the same name as we did Django will not confuss
app_name = "nameURL_4_nameSpacing_frm_urls-py"
urlpatterns = [
    #http://127.0.0.1:8000/item/
    path('item/', views.item,name='item'),     #in views.py use function helloworld #! 需要告知default urls連到這邊來
    #http://127.0.0.1:8000/
    path('', views.show,name='show'),
    #http://127.0.0.1:8000/item/1    1 is item_id cant ba any # in the table
    path('<int:item_id_frm_views_from_def_detail>/', views.detail,name="detail"),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        #! use str tried also worked
        #! <str:item_id_frm_views_from_def_detail>
#! 前面有宣告過告知default urls連到這邊來所以這個就不用打
##django has no obligation to look at this file, django will only look 
# at the urls.py which in in the prokect folder "MyFirstProject"
##C:\Users\Bruce Ashbee\Documents\MyFirstProject\MyFirstProject\urls.py
#
#* from MyFirstProject\urls.py
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('food.urls')), #! path('food/',include('food.urls')),  告知要查app [food]的urls.py 來看網址
# ]   #?path(''  >> 網址後面是空個的話 <http://127.0.0.1:8000/>
      #? 取找food app裡面的urls.py
      #?也可以不要設定是空的

#urlpatterns += staticfiles_urlpatterns()