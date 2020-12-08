from django.db import models
#! models right here actually define the structure of how these tables will be created that is 
#! these models define which columns the table would have what would be the name of the table what would
#! be the multiple fields inside the table and the data types as well.
# Create your models here.
#? go to setting.py look for  database and change the database that you wanna use

#set table name here
# class name is the table name
class Item_frm_model(models.Model):   #Primary Key is not given, django will generate filed ID automatically for us 
    def __str__(self): 
        return self.item_name #這個設定只會在查詢時顯示item_name
    #設定 table列表fields
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()


#* FYI <python shell>
#! can type commands for check table and objects
#! EXP. Item_frm_model.objects.all() will not juz show numbers of objects in the table only
#! so can show the name of object too