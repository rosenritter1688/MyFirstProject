__author__ = 'Chetan'

from datetime import datetime
import threading 

def factorial(number): 
    fact = 1

    for n in range(1, number+1): 
        fact *= n 
    return fact 

number = 100000 
thread = threading.Thread(target=factorial, args=(number,)) 
startTime = datetime.now() 
thread.start() 
thread.join() 
endTime = datetime.now() 

print ("Time for execution: ", endTime - startTime)