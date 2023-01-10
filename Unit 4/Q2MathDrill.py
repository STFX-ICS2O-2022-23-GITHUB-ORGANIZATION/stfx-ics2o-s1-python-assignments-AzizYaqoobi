import random 


userContinue = 'y'
userAnswer = 0 
num1 = 0 
num2 = 0 

print("Multiplication Questions Program!")

while userContinue == 'y' or userContinue == 'Y' :
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    
    
    
    
    while userAnswer != num1 * num2: 
        
        
        
        
        print("Answer the multiplication question: ")
        print(num1, " * ", num2, " = ", end='')
        
        
        userAnswer =int(input())
        if userAnswer == num1 * num2:
            print("correct")
        else: 
            print("incorrect") 
    userContinue = input("continue? (y/n): ")