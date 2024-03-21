from games import currency_roulette_game, guess_game, memory_game
from score import add_score

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
def welcome(username):
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey\n')

#the end of round 1, while loop until the player want to stop playing.
def want_to_play_again():
    answer = input("For play again enter 1, for exit enter 0: ")
    while answer not in ["0", "1"]:
        answer = input("This is illegal option, for play again enter 1, for exit enter 0 :")
    print()
    return (int(answer))

#the function asking for choice of game from the menu and difficulty level, and checks if they are legal
#the function returns a list of the choice and the difficulty in type int
def start_play():
    # welcome menu
    print("""Please choose a game to play:
1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2.Guess Game - guess a number and see if you chose like the computer.
3.Currency Roulette -try and guess the value of a random amount of USD in ILS
                                                                                """)
    options = ["1","2","3"]
    choice = input()
    #the checking if choice input is legal
    while choice.isnumeric() == False:
        choice = input("You need to enter a number, please enter your choice again: ")
    while choice not in options:
        choice = input("This is an illigal option, please select again: ")
    difficulty = input("Please select a difficulty level between 1 and 5: ")
    #checking if the difficulty input is legal
    difficulty_options =["1","2","3","4","5"]
    while difficulty.isnumeric() == False:
        difficulty = input("You need to enter a number, please enter your choice again: ")
    while difficulty not in difficulty_options:
        difficulty = input("This is illigal difficulty level, please select a difficulty level between 1 and 5:")
    enter_game([int(choice), int(difficulty)])
    #the end of the menu, that ask if the user want to play again
    play_again = want_to_play_again()
    if play_again == 1:
        start_play()




