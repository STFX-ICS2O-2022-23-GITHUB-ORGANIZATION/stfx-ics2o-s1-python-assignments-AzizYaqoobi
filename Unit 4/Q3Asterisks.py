import time 

ROWS = 25 
CHARS = 80 


for i in range (0, ROWS):
    for j in range (0, CHARS): 
        print("*", end = " ")
        time.sleep(0.005)
        
    print(" ")
