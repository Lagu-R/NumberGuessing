# number guessing game
# import module random and logo from art.py folder.
import random
from art import logo
from os import clear

# lvl variables 
EASY_LVL = 10
HARD_LVL = 5

# turns global variable 
turns = 0
# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        num_guess()

# Function about dificulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LVL
    else:
        return HARD_LVL
    
def game():    
    # call logo print  and greeting text.
    print(logo)
    print("Hello, this is a game where you have to try and guess the number I have come up with.")
    print("I'm thinking of a number bewteen 1 and 100.\n")
    
    # computer random number
    answer = random.randint(1, 100)
    
    # inform user about life 
    turns = set_difficulty()
    
    # repeat the code until answer = guess or turns out of remaining.
    guess = 0
    while guess != answer or turns == 0:
    # how many turn remaining 
        print(f"You have {turns} attempts remaining to guess the number.")
    # ask user number
        guess = int(input("Make a guess: "))
    #call the function of check answer
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            num_guess()
    

# ask user about play game
def num_guess():
    play_game = input("\nDo you want play guess the number? type 'y' or 'n': ").lower()
    if play_game == "y":
        clear()
        game()
    else:
        clear()
        print("Good bye <3...")
        return
num_guess()