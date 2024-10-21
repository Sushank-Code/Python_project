print("**** WELCOME TO THE QUICK QUIZ GAME *****\n")

playing = input('Do you want to paly? :')

if (playing.lower() != 'yes'):
    quit()
print("Okay ! lets play ")
score = 0

ques = input("what does CPU stands for? : ")
if (ques.lower() == 'central processing unit'):
    print("Correct")
    score += 1
else:
    print("Incorrect")

ques = input("what does GPU stands for? : ")
if (ques.lower() == 'graphic processing unit'):
    print("Correct")
    score += 1
else:
    print("Incorrect")

ques = input("what does ps stands for? : ")
if (ques.lower() == 'playstation'):
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " question correct . Thanks for playing")
