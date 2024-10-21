import random
randnumber = random.randint(1, 100)

userguess = None
guess = 0
while (userguess != randnumber):
    userguess = int(input("Enter the number "))
    guess = guess + 1
    if (userguess == randnumber):
        print(" You guessed right")
    else:
        if (userguess > randnumber):
            print("You guessed wrong. Please choose smaller number")
        else:
            print("You guessed it wrong. Please choose larger number")

print(f"You guessed it right in {guess} attempt")

with open("03highscore.txt", "r")as f:
    highscore = int(f.read())

if (guess < highscore):
    print("You have broken the highscore")
    with open("03highscore.txt", "w") as f:
        f.write(str(guess))
