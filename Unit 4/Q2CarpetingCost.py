length = 0
width = 0
cost = 0 
 

lenght = int(input("What is the lenght: "))
width = int(input("what is the width:  "))

cost = (int(lenght)  * int(width) * int(2.25))

print("The cost of the carpet per square metre " + str(lenght) + ","  +  str(width) + " is " + str(cost) + ",")