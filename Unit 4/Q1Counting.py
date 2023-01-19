# NAME OF AUTHOR:  Azizullah Yaqoobi 
# NAME OF THE PROGRAM:  Q1Counting 
# DATE OF CREATION: 2022 
# PURPOSE OF PROGRAM: counting a number by a smaller number  




# VARIABLE DEFINITION
num = 0 
num2 = 0
# INPUT
num = int(input("Enter one large number: "))
num2 = int(input("Enter the number you want to count by: "))

# PROCESSING
for num in range (num, 0, -num2):
    # OUTPUT numbers 
    print(num)