#Number Guessing Game Objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
# Include an ASCII art logo.
import random
from replit import clear

# Global difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# Add the logo
print(logo)

# Set difficulty level
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  elif difficulty == "hard":
    return HARD_LEVEL_TURNS

# Function to check the user's guess
def check_guess(guess, number, turns):
  if guess == number:
      print(f"You got it! The answer was {number}.")
      answer = input("Do you want to play again? Yes or no? ").lower()
      if answer == "yes":
        clear()
        guessing_game()
      else:
        print("Goodbye!")
        exit()
  elif guess > number:
      print("Too high.")
      return turns - 1
  elif guess < number:
      print("Too low.")
      return turns - 1



def guessing_game():
  # Welcome message and instructions for the game
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1, 100)
  print(f"Pssst, the correct answer is {number}")

  # Set the number of attempts
  turns = set_difficulty()
  guess = 0
  
  # Check the user's guess and reduce the number of attempts by 1 if the guess is incorrect
  while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")
    # Check if the user has run out of attempts and end the game if they have run out of attempts
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return

    # Let the user guess the number and check the guess against the number
    guess = int(input("Make a guess: "))
    turns = check_guess(guess, number, turns)
    
    
guessing_game()
  

