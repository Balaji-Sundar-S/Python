import random

def game () :

    print(f"welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
    choice = input ("choose a difficulty. Type 'easy' or 'hard': ")
    if choice.lower() == 'easy' :
        easy()
    else :
        hard()

def easy () :

    i = 0
    N = 10
    while i < 10 :
        print (f"you have {N} attempts remaining to guess the number.")
        guess = int (input ("Make a guess : "))
        if guess < random_number :
            print (f"Too low.")
        elif guess > random_number :
            print (f"Too high.")
        elif guess == random_number :
            print (f"you got it! The answer was {guess}")
            exit()
        i += 1
        N -=1
    print (f"you've run out of guesses, you lose.\nThe number is {random_number}.")

def hard () :

    i = 0
    M = 5
    while i < 5 :
        print (f"you have {M} attempts remaining to guess the number.")
        guess = int (input ("Make a guess : "))
        if guess < random_number :
            print (f"Too low.")
        elif guess > random_number :
            print (f"Too high.")
        elif guess == random_number :
            print (f"you got it! The answer was {guess}")
            exit()
        i += 1
        M -= 1
    print (f"you've run out of guesses, you lose.\nThe number is {random_number}.")

random_number = random.randint(1, 100)
game ()    