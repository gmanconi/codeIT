# True or False quiz program
# For the London Metropolitan University Code-It challenge 2022

import library
import time
import os
quiz_name = ["Geography", "History", "Programming (Phyton Based)"]
quiz_code = ["1", "2", "3"]
flow_control = ""
answers = []
geography_scores = []
history_scores = []
programming_scores = []

import os
if os.name == "posix":
    clear_screen = "clear"
else:
    clear_screen = "cls"
    
library.spacer()
print("*Welcome to 'QUIZZER'*")
library.spacer()
library.enter()
library.spacer()
scores = []
while flow_control != "3":
    
    flow_control = library.main()
    library.spacer()
    if flow_control == "1":
        chosen_quiz = library.drop_down_list(quiz_code[0], quiz_name[0], quiz_code[1], quiz_name[1], quiz_code[2], quiz_name[2])
        library.spacer
        if chosen_quiz == "1":
            os.system(clear_screen)
            print("You decided to take a", quiz_name[0], "quiz\nGood Luck!")
            library.spacer()
            library.enter()
            library.spacer()
            from library import geography_q
            score = library.quiz(geography_q[0], geography_q[1], geography_q[2], geography_q[3], geography_q[4], geography_q[5], geography_q[6], geography_q[7], geography_q[8], geography_q[9])
            geography_scores.append(score)
            os.system(clear_screen)
        elif chosen_quiz == "2":
            os.system(clear_screen)
            print("You decided to take a", quiz_name[1], "quiz\nGood Luck!")
            library.spacer()
            library.enter()
            library.spacer()
            from library import history_q
            score = library.quiz(history_q[0], history_q[1], history_q[2], history_q[3], history_q[4], history_q[5], history_q[6], history_q[7], history_q[8], history_q[9])
            history_scores.append(score)
            os.system(clear_screen)
        elif chosen_quiz == "3":
            os.system(clear_screen)
            print("You decided to take a", quiz_name[2], "quiz\nGood Luck!")
            library.spacer()
            library.enter()
            library.spacer()
            from library import programming_q
            score = library.quiz(programming_q[0], programming_q[1], programming_q[2], programming_q[3], programming_q[4], programming_q[5], programming_q[6], programming_q[7], programming_q[8], programming_q[9])
            programming_scores.append(score)
            os.system(clear_screen)
            
    elif flow_control == "2":
        chosen_score = library.scores_menu(quiz_code[0], quiz_name[0], quiz_code[1], quiz_name[1], quiz_code[2], quiz_name[2])
        if chosen_score == "1":
            os.system(clear_screen)
            print("You decided to display", quiz_name[0], "scores!")
            library.spacer()
            library.enter()
            library.spacer()
            scores = library.score_display(geography_scores, quiz_name[0])
            
        elif chosen_score == "2":
            os.system(clear_screen)
            print("You decided to display", quiz_name[1], "scores!")
            library.spacer()
            library.enter()
            library.spacer()
            scores = library.score_display(history_scores, quiz_name[1])

        elif chosen_score == "3":
            os.system(clear_screen)
            print("You decided to display", quiz_name[2], "scores!")
            library.spacer()
            library.enter()
            library.spacer()
            scores = library.score_display(programming_scores, quiz_name[2])
            
            
