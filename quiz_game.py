print("WELCOME TO MY SIMPLE QUIZ GAME")

play = input("Do you want to play the game?\n")

if play.lower() == "no":
    quit()

score = 0
   
answer = input("What is the capital of Japan?\n")
if answer.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("False")
    
answer = input("What is the formula of water?\n")

if answer.lower() == "h2o":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("How many continents are there on Earth?\n")
if answer.lower() == "7" or answer.lower() == "seven":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What planet is known as the Red Planet?\n")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which language is most widely spoken in the world?\n")
if answer.lower() == "english":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')
    
print(f"Your score is: {score}")
print(f"You got {(score/5)*100} %.")
    


    