# function library
answers = []
geography_q = ["The capital of Italy is Milan\na) True\nb) False\n",
               "The Red Sea is in USA\na) True\nb) False\n",
               "London is the capital of Wales\na) True\nb) False\n",
               "Paris is the capital of France\na) True\nb) False\n",
               "The Loire Valley is in Poland\na) True\nb) False\n",
               "Washington DC is in USA\na) True\nb) False\n",
               "The Sahara desert is in Africa\na) True\nb) False\n",
               "The Mediterrenean sea touches Germany\na) True\nb) False\n",
               "Stoneage is in Libia\na) True\nb) False\n",
               "The Po river is in Italy\na) True\nb) False\n"]

history_q = ["The Ancient Roman empire started in Germany\na) True\nb) False\n",
             "The WW1 started in 1906\na) True\nb) False\n",
             "British empire never reached India\na) True\nb) False\n",
             "Rome was founded the 21 April 753 BC\na) True\nb) False\n",
             "300 Solidiers held off the Persians at Thermopylae for three days\na) True\nb) False\n",
             "The great Pyramid of Giza as been constructed during the 4th dynasty\na) True\nb) False\n",
             "Alexander The Great died at the age of 32\na) True\nb) False\n",
             "The WW2 started the 1st September 1930\na) True\nb) False\n",
             "Columbus was not the first European to sail to Americas\na) True\nb) False\n",
             "California and Texas were once part of Mexico\na) True\nb) False\n"]

programming_q = ["The secondary Memory is called RAM\na) True\nb) False\n",
                 "Keywords make good variable names\na) True\nb) False\n",
                "In Python this statement is legal: print(2 + '2')\na) True\nb) False\n",
                 "A counted loop is designed to iterate a specific number of times\na) True\nb) False\n",
                 "In Phyton 2 + 2.0 = 2\na) True\nb) False\n",
                 "A Phyton list is mutable\na) True\nb) False\n",
                 "The sum between integers and floating will always return a floating as result\na) True\nb) False\n",
                 "Phyton is a non case sensitive language\na) True\nb) False\n",
                 "Phyton is a low level language\na) True\nb) False\n",
                 "Phyton is an object oriented language\na) True\nb) False\n"]

correct_answers= ["B", "B", "B", "A", "B", "A", "A", "B", "B", "A"]


def enter():
    input("Press ENTER to move forward")

def spacer():
    print("**************************************")

def drop_down_list(c1, n1, c2, n2, c3, n3):
    print("List of quiz to take:")
    print("",c1, "--->", n1,"\n", c2,  "--->", n2,"\n", c3,  "--->", n3)
    quiz_select = input("Select the test to take by writing the corresponding number\n")
    return quiz_select

def main():
    flow_c = input("Select action:\n1: Show aviable quiz\n2: Show previous scores\n3: Quit the program\n")
    return flow_c

def quiz(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 ):
    counter = -1
    score = 0
    print("This is a True / False quiz, answer writing a/b only")
    print("**************************************")
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for question in questions:
        counter += 1
        q_1 = input(question)
        print("**************************************")
        q_1 = q_1.upper()
        answers.append(q_1)
        if answers[counter] == correct_answers[counter]:
            score += 1
            print("Correct answer!")
            print("**************************************")
        else:
            print("Wrong answer")
            print("**************************************")
    answers.clear()
    return score

def scores_menu(c1, n1, c2, n2, c3, n3):
    print("Display score of the following quizzes:")
    print("",c1, "--->", n1,"\n", c2,  "--->", n2,"\n", c3,  "--->", n3)
    score_select = input("Select the scores to display by writing the corresponding number\n")
    return score_select                      

def score_display(scores_list, name):
    counter = 0
    if len(scores_list) != 0:
        print("You have", len(scores_list), "scores saved for", name)
        print("**************************************")
        for i in scores_list:
              counter += 1
              print("Score N", counter, ":", scores_list[counter - 1])
              print("**************************************")
    else:
        print("You have no scores saved for", name)
        print("**************************************")
        
