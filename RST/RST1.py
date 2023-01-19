# NAME OF AUTHOR: Azizullah Yaqoobi 
# NAME OF THE PROGRAM: Rock, paper, and scissors game  
# DATE OF CREATION: 2023, 01, 18
# PURPOSE OF PROGRAM: to play the rock, paper and scissors game alone. 



import random
while True:
    # VARIABLE DEFINITION
    options = ("rock", "paper", "scissors")
    player = None
     # Generate a random choice from the options 
    computer = random.choice(options)
    # INPUT
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    # OUTPUT
    print(f"player: {player}")
    print(f"computer: {computer}: ")
    # PROCESSING
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
   
    play_again = input("Do you want to play again? (yes/no)")
    if play_again.lower() == "no":
        break
