from django.db import models
#! models right here actually define the structure of how these tables will be created that is 
#! these models define which columns the table would have what would be the name of the table what would
#! be the multiple fields inside the table and the data types as well.
# Create your models here.
#todo go to setting.py look for  database and change the database that you wanna use
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

class item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    iten_price = models.IntegerField()