## `C:\Users\Bruce Ashbee\Documents\MyFirstProject\MyFirstProject\settings.py`
## app with database required
![pic07](img/07.png)

#first command
`Python manage.py makemigrations food`
![command 1](img/10.png)
#sec command
> Python manage.py sqlmigrate food 0001
### 0001 is看上面的圖 food\migrations\0001_initail.py

![command 2](img/11.png)
#CAUTION !! Django 自動幫我們弄了PRIMARY KEY id

`pyhon manage.py migrate`
![command 3](img/12.png)
## the migrate command which is actually going to create the table for us.

![idea](img/13.png)
![idea2](img/14.png) #to create an object![idea3](img/14-2.png)#use save() to save object to table