highestMark = 0 
lowestMark = 100 
userContinue = "Y"
userMark = 0 
marksRange = 0 


while(userContinue == "Y" ) or (userContinue == "y"):
    userMark = int(input("Enter your Mark: "))
    
    if userMark > highestMark:
        highestMark = userMark
    
    
    if userMark < lowestMark:
        lowestMark = userMark 
    
    userContinue = input("continue? (Y/n): ")
    
    
marksRange = highestMark - lowestMark 

print("your range is " + str(marksRange))