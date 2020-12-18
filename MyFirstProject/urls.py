"""MyFirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')), #! path('food/',include('food.urls')),  告知要查app [food]的urls.py 來看網址
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#! path('', include('food.urls')),
#? if http://127.0.0.1:8000/ will look for urls.py under food app
#! the main point is path(''
"""
from . import views #     . means current directory     <import views.py>
from django.urls import path


urlpatterns = [
    path('hello/', views.helloworld,name='helloworld'),     #in views.py use function helloworld #! 需要告知default urls連到這邊來
    path('item/',views.item,name='item'),
]
"""
#? what will works now is http://127.0.0.1:8000/hello/
#?                        http://127.0.0.1:8000/item/

#! if i set path('food', include('food.urls')),
#! what will works now is http://127.0.0.1:8000/food/hello/
#!                        http://127.0.0.1:8000/food/item/ 

