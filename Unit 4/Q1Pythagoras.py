leg1 = 0 
leg2 = 0 
leg3 = 0 
from math import sqrt 
leg1 = int(input("what is the first leg of triangle: "))
leg2 = int(input("what is the second leg of triangle: "))
leg3 = sqrt(leg1 ** 2 + leg2 ** 2 )

print("The right angle of this Triangle is")
print(leg3)