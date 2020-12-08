from django.contrib import admin

# Register your models here.

from food.models import Item_frm_model   #!from current directory use models.py and import table Item
#same as 
#from .models import Item_frm_model
admin.site.register(Item_frm_model)  #! add anything u wanna show in http://127.0.0.1:8000/admin/
