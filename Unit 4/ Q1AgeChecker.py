# NAME OF AUTHOR:  Azizullah Yaqoobi 
# NAME OF THE PROGRAM: Age Checker 
# DATE OF CREATION: 2023_01_11
# PURPOSE OF PROGRAM:  where should you be according to your age. 
# OUTPUT  = where they belong to 




# VARIABLE DEFINITION

ElementaryAgeLow = 5
ElementaryAgeHigh = 11
IntermediateAgeLow = 12
IntermediateAgeHigh = 14 
HighschoolAgeLow = 15
HighschoolAgeHigh = 18
Higher = 19 
age = 0 

# INPUT
age = int(input("What is your age? "))


# PROCESSING
if age < ElementaryAgeLow: 
    print("You are too young for school")
if (age >= ElementaryAgeLow) and (age <= ElementaryAgeHigh):
    print("You are in elementary school.")
if (age >= IntermediateAgeLow) and (age <= IntermediateAgeHigh):
    print("You are in Intermediate school.")
if (age >= HighschoolAgeLow) and (age <= HighschoolAgeHigh):
    print("You are in High school")
    
if (age >= Higher):
    print("You are in University, College, or the Work force")