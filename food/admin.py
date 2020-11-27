from django.contrib import admin

# Register your models here.

from food.models import Item   #!from current directory use models.py and import table Item
#same as 
#from .models import Item
admin.site.register(Item)  #! add anything u wanna show in http://127.0.0.1:8000/admin/
