# NAME OF AUTHOR:  Azizullah Yaqoobi 
# NAME OF THE PROGRAM:  Q3Primes 
# DATE OF CREATION:  2023_01_10 
# PURPOSE OF PROGRAM: Find the Prime numbers between two number  


# INPUT
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
# OUTPUT
print ("The Prime Numbers in the range are: ")  
# PROCESSING
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  