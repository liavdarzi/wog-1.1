import os

#the variabels
score_file_name = "scores.txt"
bad_return_code = 404

#function that clean the screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
