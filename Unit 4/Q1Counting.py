num = 0 
num2 = 0

num = int(input("Enter one large number: "))
num2 = int(input("Enter the number you want to count by: "))


for num in range (num, 0, -num2):
    
    print(num)