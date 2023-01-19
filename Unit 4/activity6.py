# NAME OF AUTHOR: Azizullah Yaqoobi  
# NAME OF THE PROGRAM: RST => the activity6  
# DATE OF CREATION: 2023. 01. 16 
# PURPOSE OF PROGRAM: engaging the number guessing game 

while True:
  num1 = 0
  num2 = 0
  num3 = 0
 
  num1 = int(input("Enter your first number: "))
  num2 = int(input("Enter your first number: "))
 
  import random
 
  # Generate a random number between
  n = random.randint(num1, num2)
 
  # Keep track of the number of guesses
  var = 0
 
  while True:
      # Get the user's guess
      num3 = int(input("Guess a number between the two number you entered: "))
 
      # Increase the number of guesses
      var += 1
 
      # Check if the guess is correct
      if num3 == n:
          print("Congratulations! You guessed the number in", var, "guesses!")
          break
      elif num3 < n:
          print("Too low!")
      else:
          print("Too high!")
  play_again = input("Do you want to play again? (yes/no)")
  if play_again.lower() == "yes":
        continue
  else:
      print("Thank you for playing!")
      break
