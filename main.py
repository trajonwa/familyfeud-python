import os
from time import sleep, time
from gtts import gTTS
from classes import GameCard
from classes import Board
from classes import Team

### Current Issues ###

# Not sure how to handle synoynms/similar answers
# When you guess all the answers correctly without hitting the 3 missed answers, it still asks for answers
    # Probably because the list_of_answers that the inner while loop is running off isn't being decremented to zero?

'''
Variables and Two Functions for the game
'''
is_running = True
temp_score = 0
missed_answers = 0
answer = ""
round = 0


def instructions():
    """
    This function uses the instructions file to display the game rules to the teams.
    """
    file = open("Instructions.txt", "r")
    for line in file:
        print(line)
        sleep(2)
    file.close()

# Function to toggle to the current team based on the current round
def get_current_team():
    players = [first_team, second_team]
    return players[round % len(players)]

# Function to toggle to the next team based on the current round
def get_next_team():
    players = [first_team, second_team]
    return players[(round + 1) % len(players)]

# Function that clears the screen and prints all the game info on the screen 
def refresh_screen(duration=1.5):
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
        sleep(duration)
        print(f"Round Score: {temp_score}")
        print(f"{first_team.name}'s Score: {first_team.score} | {second_team.name}'s Score: {second_team.score}")
        board.print_board()

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

# This list just contains a list of the answers in order to print said answers instead of using the dictionary.
list_of_answers = []

# Appends each answer to the list of answers. Note that the answers are the keys to the GameCard object's dictionary.
for keys in card0.answers:
    list_of_answers.append(keys)

'''
Main Game Below
'''
print("Welcome to Family Feud!")
print()
instructions()

# Asks for the teams' names and creates a Team object using the inputs.
first_team = Team(input("Team 1, Enter your name here: "))
second_team = Team(input("Team 2, Enter your name here: "))

# Main while loop for the game.
while is_running:

    # Creates a board and builds the board using the length of the number of answers.
    board = Board()
    board.build_board(len(card0.answers))

    # for loops that does two rounds
    for x in range(2):

        # gets the current team and stores the current team in a variable to be used. 
        current_team = get_current_team()

        while len(list_of_answers) != 0:
            refresh_screen()
            print(card0.question)
            answer = input(f"{current_team.name}, What is your answer: ")
            print()
            if missed_answers == 2:
                print(f"Oops, you've guessed incorrectly three times! It's {get_next_team().name}'s turn!")
                current_team = get_next_team() # Since the current play team missed three times, the current team is now the next team.
                sleep(2)
                break
            elif answer.upper() not in list_of_answers:
                missed_answers += 1
                print("Oops, wrong answer!")
                sleep(2)
            else:                  
                print("You got it!")
                index = list_of_answers.index(answer.upper()) # Gets the index of the answer from the list of answers and stores it.
                board.board[index] = answer.upper() + " " + str(card0.answers[answer.upper()][0]) # stores the answer with the score on the board given the index
                temp_score += card0.answers[answer.upper()][0] # take the score and add it to the temporary score variable
                sleep(2)

        missed_answers = 0

        # As it states, this is going to ALWAYS be true because I'm not decrementing the list_of_answers. Needs to be fixed.
        if len(list_of_answers) != 0:
            refresh_screen()
            answer = input(f"{current_team.name}, What is your answer: ")
            print(card0.question)

            if answer.upper() in list_of_answers:
                # If the answer is correct, like for the first team in the round, we just get the index,
                # then store the answer with the score on the board using that index. 
                # Then take the score and add it to the temporary score and give it to the stealing team.
                # Then we just refresh the screen say they won and reset the temporary score.
                index = list_of_answers.index(answer.upper())
                board.board[index] = answer.upper() + " " + str(card0.answers[answer.upper()][0])
                temp_score += card0.answers[answer.upper()][0]
                current_team.score = temp_score
                refresh_screen()
                print(f"{current_team.name} has won the round!")
                temp_score = 0
                sleep(3)
            else:
                # If the stealing team, got it wrong, then we just give the first team the total score, refresh the screen
                # sand say they won. Then reset the temporary score.
                get_current_team().score = temp_score
                refresh_screen()
                print(f"{get_current_team().name} has won the round!")
                temp_score = 0
                sleep(3)
        
    print("Do you want to play two more rounds? ")
