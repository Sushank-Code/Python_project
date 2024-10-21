import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

def main():
    while True:
        play_game()
        
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
