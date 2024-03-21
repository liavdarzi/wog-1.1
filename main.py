from app import start_play,welcome
from score import delete_score

#to make sure that the score is 0 before the game starts
delete_score()
user_name = input("Please enter your username: ")
welcome(user_name)
#round 1
start_play()
print(f"Thank you for playing {user_name}!")

