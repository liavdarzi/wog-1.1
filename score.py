from utils import score_file_name

#the function presents the current score
def current_scores():
    with open(score_file_name, "r") as scores_file:
        current_score = scores_file.read()
        #reset the score to 0 if the file is empty
        if current_score == "":
            current_score = 0
        else:
            current_score = int(current_score)
        return current_score

#the function read the current score from the scores file, and save the new current score
def add_score(difficulty):
    point_of_winning = difficulty * 3 + 5
    current_score = current_scores()
    current_score = current_score + point_of_winning
    with open(score_file_name,"w") as scores_file:
        scores_file.write(str(current_score))
    print(f"Your current score is: {current_score}")

#the function reset the score to 0
def delete_score():
    with open(score_file_name,"w") as score_file:
        score_file.write("0")

