from classes import GameCard
from classes import Board
from classes import Team

### Current Issues ###

# Not sure how to handle synoynms/similar answers
# You guess incorrectly four times instead of three based on the current while loop
# Whenever the answers are printing on screen, there are some annoying spaces



'''
Variables and Two Functions for the game
'''
is_running = True
temp_score = 0
missed_answers = 0
answer = ""
round = 0
first_team = ""
second_team = ""

def get_current_team():
    players = [first_team, second_team]
    return players[round % len(players)]

def get_next_team():
    players = [first_team, second_team]
    return players[(round + 1) % len(players)]

'''
Temp Data Below
'''

card0 = GameCard("In Horror Movies, Name a Place Teenagers Go Where There’s Always a Killer On the Loose")
card0.answers["CABIN"] = (49, ("CAMP", "WOODS"))
card0.answers["GRAVEYARD"] = (12, ())
card0.answers["MOVIE THEATRE"] = (6, ("DRIVE-IN"))
card0.answers["BASEMENT"] = (6, ("CELLAR"))
card0.answers["CLOSET"] = (5, ())
card0.answers["BATHROOM"] = (4, ("SHOWER"))
card0.answers["BEDROOM"] = (4, ("BED"))
card0.answers["PARTY"] = (4, ())

list_of_answers = []

for keys in card0.answers:
    list_of_answers.append(keys)

'''
Main Game Below
'''
print("Welcome to Family Feud!")

first_team = input("Team 1, Enter your name here: ")
second_team = input("Team 2, Enter your name here: ")

while is_running:
    board = Board()
    board.build_board(len(card0.answers))

    for x in range(2):

        current_team = get_current_team()

        while len(list_of_answers) != 0:
            board.print_board()
            answer = input(f"{current_team}, What is your answer: ")
            print()
            if missed_answers == 3:
                print("Oops, you've guessed incorrectly three times!")
                current_team = get_next_team()
                break
            elif answer.upper() not in list_of_answers:
                missed_answers += 1
                print("Oops, wrong answer!")
            else:                  
                print("You got it!")
                index = list_of_answers.index(answer.upper())
                board.board[index] = answer.upper() + " " + str(card0.answers[answer.upper()][0])
                temp_score = card0.answers[answer.upper()][0]
        
        missed_answers = 0
        if len(list_of_answers) != 0:
            answer = input(f"{current_team}, What is your answer: ")

            if answer:
                # assign score to opposing team
                temp_score = 0
            else:
                # assign score to current team
                temp_score = 0
        
    print("Do you want to play two more rounds? ")