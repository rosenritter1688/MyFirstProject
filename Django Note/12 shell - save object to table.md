## open python shell
`python manage.py shell`

![command 1](img/15.png)

### enter 
`from food .models import Item`
# 名字已經變更為Item coz of problems名字已經變更為Item coz of problems

![command 2](img/16.png)
`item.objects.all()`
### Checking objects in the table 
###<QuerySet []>  means the table is empty
####another example
#![example](img/19.png)



## save ojects into table
###check first`C:\Users\Bruce Ashbee\Documents\MyFirstProject\food\models.py`


![pic](\img\06.png)
![command 3](img/17.png)
`a = Item(item_name="Pizza",item_desc="Cheesy Pizza",item_price = 20)`
### name the object as a 

![command 4](img/18.png)

###use save() function to save a to table

