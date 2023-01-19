# NAME OF AUTHOR: Azizullah Yaqoobi  
# NAME OF THE PROGRAM:  Q1Pythagoras 
# DATE OF CREATION: 2022. 12. 06 
# PURPOSE OF PROGRAM:  

# VARIABLE DEFINITION
leg1 = 0 
leg2 = 0 
leg3 = 0 
# INPUT
from math import sqrt 
leg1 = int(input("what is the first leg of triangle: "))
leg2 = int(input("what is the second leg of triangle: "))
# PROCESSING
leg3 = sqrt(leg1 ** 2 + leg2 ** 2 )
# OUTPUT
print("The right angle of this Triangle is")
print(leg3)