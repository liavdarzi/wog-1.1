from games import currency_roulette_game, guess_game, memory_game
from score import add_score, delete_score

def enter_game(choice_difficulty_list):
    choice = choice_difficulty_list[0]
    difficulty = choice_difficulty_list[1]
    if choice == 1:
        memory_game.play(difficulty)
    elif choice == 2:
        guess_game.play(difficulty)
    elif choice == 3:
        currency_roulette_game.play(difficulty)

# welcome function, that print a welcome massage
def welcome():
    # to make sure that the score is 0 before the game starts
    delete_score()
    user_name = input("Please enter your username: ")
    print(f'Hi {user_name} and welcome to the World of Games: The Epic Journey\n')

#the end of round 1, while loop until the player want to stop playing.
def want_to_play_again():
    answer = input("For play again enter 1, for exit enter 0: ")
    while answer not in ["0", "1"]:
        answer = input("This is illegal option, for play again enter 1, for exit enter 0 :")
    if answer == "1":
        print()
        start_play()
    else:
        print(f"Thank you for playing !")

# checking if the input is numeric and if he is in the options list, using while loop untill its llegal
def llegal_input(var, options):
    while var.isnumeric() == False or var not in options:
        var = input("You need to enter a number between the options, please enter your choice again: ")
    return int(var)

#the function asking for choice of game from the menu and difficulty level
#the function enter a list of the choice and the difficulty in type int
def start_play():
    # welcome menu
    print("""Please choose a game to play:
1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2.Guess Game - guess a number and see if you chose like the computer.
3.Currency Roulette -try and guess the value of a random amount of USD in ILS
                                                                                """)
    choice = input()
    choice = llegal_input(choice,["1","2","3"])
    difficulty = input("Please select a difficulty level between 1 and 5: ")
    difficulty = llegal_input(difficulty,["1","2","3","4","5"])
    enter_game([choice, difficulty])
    #the end of the menu, that ask if the user want to play again
    want_to_play_again()


