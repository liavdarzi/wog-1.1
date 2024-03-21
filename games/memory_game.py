import random
import time
from score import add_score,current_scores
from utils import screen_cleaner

#function that clean the screen, print the list of the memory numbers, and clean the screen again
def print_and_disappear(game_list):
    screen_cleaner()
    print(game_list)
    time.sleep(0.7)  # disappear for 1 second
    #clear for windows and linux
    screen_cleaner()

#Generates a list of random numbers between 1 and 101, with a length equal to the difficulty.
def generate_sequence(difficulty):
    game_list = []
    for i in range(difficulty):
        select_number = random.randint(1,101)
        game_list.append(select_number)
    return game_list

#Prompts the user to input a list of numbers matching the length of the generated sequence.
def get_list_from_user(difficulty):
    print(f'Now you need to enter {difficulty} numbers, the numbers must be a number between 1 and 100.')
    user_list = []
    #not importent number just to enter to the while loop.
    number = 2
    while len(user_list) < difficulty:
        number = input("Please enter a number: ")
        while number.isnumeric() == False:
            number = input("The number is illegal, the input must to be a number : ")
        while not (1<=int(number) and int(number)<= 100) :
            number = input("The number is illegal, the numbers must be a number between 1 and 100 : ")
            #just if the user enter a string again, define number to enter again to the loop
            if number.isnumeric() == False:
                number = 102
        user_list.append(int(number))
    print(f'Your list is {user_list}')
    return user_list

#Compares two lists to verify if they are identical, returning True if they match and False otherwise.
def is_list_equal(difficulty, game_list, user_list):
    is_equel = True
    for i in range(difficulty):
        if game_list[i] == user_list[i]:
            continue
        else:
            is_equel =False
            break
    return is_equel

def play(difficulty):
    print(f'''
WELCOME to the memory game! You are playing in difficulty {difficulty}!
You will get a list of {difficulty} numbers that will disappear in 0.7 seconds: 
    ''')
    time.sleep(5)
    game_list = generate_sequence(difficulty)
    print_and_disappear(game_list)
    user_list = get_list_from_user(difficulty)
    result = is_list_equal(difficulty, game_list, user_list)
    print(f"The list of the computer is {game_list}")
    if result == True:
        print("Congratulations! you are the winner!")
        add_score(difficulty)
    else:
        print("You are the looser for now, maybe next time :) ")
