# Rock , Paper ,scissor 

import random

def user_input(choice):
    if(choice == "r"):
        print("You choose Rock")
    elif(choice == "p"):
        print("You choose Paper")
    else:
        print("You choose Scissor")


def computer_input(c_choice):
    if(c_choice == "r"):
        print("Computer choose Rock")
    elif(c_choice == "p"):
        print("Computer choose Paper")
    else:
        print("Computer choose Scissor")
    
    
def gamelogic(c_in,user_in):
    if(c_in == user_in):
        print("Tie")
    elif (c_in == "r" and user_in == "s") or \
         (c_in == "s" and user_in == "p") or \
         (c_in == "p" and user_in == "r"):
        print("You lose!")
    else:
        print("You win!")

def play_game():
    user_choice = input("Enter 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
    game = ['r', 'p', 's']
    computer_choice = random.choice(game)

    user_input(user_choice)
    computer_input(computer_choice)
    gamelogic(computer_choice,user_choice)

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break

main()



