import random
from score import add_score,current_scores

# Generates a random number between 0 and the specified difficulty, and saving it as the secret_number.
def generate_number(difficulty):
    sectet_number = random.randint(0, difficulty)
    return sectet_number

#Prompts the user to input a number within the range of 0 to the difficulty and returns the entered number.
def get_guess_from_user(difficulty):
    guess = input(f'Guess a number between 0 and your difficulty- {difficulty} include: ')
    #checking if the input is legal
    while guess.isnumeric() == False or ( int(guess)< 0 or int(guess)> difficulty ):
        guess = input("Your guess is illegal, please guess again a number between 0 and your difficulty: ")
    return int(guess)

#compare_results: Compares the generated secret number with the user's input and determines if they match.
def compare_results(secret_num, guess):
    #making sure that the types are equal for comparing
    if type(secret_num)!= type(guess):
        secret_num = int(secret_num)
        guess = int(guess)
    print(f'Your guess: {guess}, the secret number: {secret_num}')
    if secret_num == guess:
        return True
    else:
        return False

def play(difficulty):
    print()
    print(f'WELCOME to the Guess Game! You are playing in difficulty {difficulty}!')
    guess = get_guess_from_user(difficulty)
    secret_number = generate_number(difficulty)
    result = compare_results(secret_number,guess)
    if result == True:
        print("You are the winner!")
        add_score(difficulty)
    else:
        print("You lose, maybe next time! ")
    return result



