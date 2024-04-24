from art import logo, vs    # import the logo and vs from art.py
from game_data import data  # import the game data from game_data.py
from replit import clear    # import the clear function from replit module to clear the screen between rounds 
import random               # import the random module to generate random numbers for the game


# Generate a random account from the game data
def random_account():
  return random.choice(data)


# Format the account data into printable format
def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Print the logo
print(logo)
# Starting score of the game is 0
score = 0
# Make the game continue as long as the user is correct
game_should_continue = True
# Generate a random account from the game data and assign it to account_b

account_b = random_account()

# Make game repeatable
while game_should_continue:
  
  # Make B become the next A
  account_a = account_b
  account_b = random_account()

  while account_a == account_b:
    account_b = random_account()

  print(f"Compare A: {format_data(account_a)}.")
  print(vs) # print the vs logo between the two accounts
  print(f"Against B: {format_data(account_b)}.")

  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  ## Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  # Check if they are correct or not
  ## Use if statement to check if user is correct
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen between rounds and print the logo
  clear()
  print(logo)

  # Give user feedback on their guess
  if is_correct:
    score += 1
    print(f"You're right! You guessed correctly. Current score: {score}.")
  else:
    print("Sorry, that's wrong. Game Over.")
    print(f"Final score: {score}")
    game_should_continue = False



