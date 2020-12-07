from django.db import models
#! models right here actually define the structure of how these tables will be created that is 
#! these models define which columns the table would have what would be the name of the table what would
#! be the multiple fields inside the table and the data types as well.
# Create your models here.
#? go to setting.py look for  database and change the database that you wanna use
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

class Item(models.Model):   #Primary Key is not given, django will generate filed ID automatically for us 
    
    #! add a function so under python shell
    #! command Item.objects.all() will not juz show numbers of objects in the table only
    #! so can show the name of object too
    def __str__(self):   #? so when we 在python shell(12.sehll save object)打Item.objects.all 才可查有多少object 在table "Item"裡面
        #return self.item_name,self.item_desc,self.item_price
        #! 不可以這樣用
        #! TypeError: __str__ returned non-string (type tuple)
        #? cannt show more than one variable if using __str__
        return self.item_name


    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()