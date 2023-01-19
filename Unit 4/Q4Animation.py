var1 = 0 
var2 = 0 
var3 = 0 


var1 = int(input("Enter you first number: "))
var2 = int(input("Enter you first number: "))

import random
n = random.randrange(var1, var2)
var3 = int(input("Enter any number: "))
while n!= var3:
    
    if var3 < n:
        print("Incorrect!")
        var3 = int(input("Enter number again: "))
    elif var3 > n:
        print("Incorrect!")
        var3 = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")