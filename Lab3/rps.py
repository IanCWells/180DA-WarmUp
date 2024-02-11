import random
rock = 0
paper = 1
scissors = 2



def playagain():
    start = str(input("Wanna play again? (y/n): "))
    if(start == 'y' or start == 'Y'):
        game()
    else: 
        print("See you later")   

def game():
    print("I've got my answer!")
    random_number = random.randint(0, 2)
    answer = str(input(("What is yours? Type r/p/s for rock paper or scissors: ")))
    
    if(answer == 'r'):
        if(random_number == 0):
            print("Ive got rock, tie!")
        if(random_number == 1):
            print("Ive got paper, you lose!")
        if(random_number == 2):
            print("Ive got scissors, you win!")
    elif(answer == 'p'):
        if(random_number == 0):
            print("Ive got rock, you win!")
        if(random_number == 1):
            print("Ive got paper, tie!")
        if(random_number == 2):
            print("Ive got scissors, you lose!")
    elif(answer == 's'):
        if(random_number == 0):
            print("Ive got rock, you lose!")
        if(random_number == 1):
            print("Ive got paper, you win!")
        if(random_number == 2):
            print("Ive got scissors, tie!")
    else:
        print("That's not an answer :(")
        playagain()
        

print("Rock Paper Scissors Game")

start = str(input("Ready? (y/n): "))
if(start == 'y' or start == 'Y'):
    game()
else: 
    print("See you later")   