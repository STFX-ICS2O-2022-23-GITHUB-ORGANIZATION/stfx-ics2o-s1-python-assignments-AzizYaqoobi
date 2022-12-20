import random 


userContinue = 'y'
userAnswer = 0 
num1 = 0 
num2 = 0 

print("Addition Questions Program!")

while userContinue == 'y' or userContinue == 'Y' :
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    
    
    
    while userAnswer != num1 + num2: 
        
        
        # user prompt 
        
        print("Answer the Addition question: ")
        print(num1, " + ", num2, " = ", end='')
        
        
        userAnswer =int(input())
        
    userContinue = input("continue? (y/n): ")