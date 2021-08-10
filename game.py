import os
import random
import classes
from time import sleep, time
from classes import GameCard
from classes import Board
from classes import Team

'''
### Current Issues ###

- Game may crash when it runs out of cards. Will fix this soon.

### Things To Implement ###
- Show all remaining answers after the round is over.

### Fixed - 8/10 ###
- Implemented a solution to look for similar answers
- Fixed the bug where it allows users to put the same answer twice or more

'''


# Temp Data Below

# Card 1

card0 = GameCard("In Horror Movies, Name a Place Teenagers Go Where There’s Always a Killer On the Loose")
card0.answers["CABIN"] = (49, {"CAMP", "WOODS"})
card0.answers["GRAVEYARD"] = (12, {})
card0.answers["MOVIE THEATRE"] = (11, {"DRIVE-IN"})
card0.answers["BASEMENT"] = (11, {"CELLAR"})
card0.answers["CLOSET"] = (5, {})
card0.answers["BATHROOM"] = (4, {"SHOWER"})
card0.answers["BEDROOM"] = (4, {"BED"})
card0.answers["PARTY"] = (4, {})

# Card 2
'''
card1 = GameCard("Name Marvel’s Avengers")
card1.answers["CAPTAIN AMERICA"] = (22, {})
card1.answers["IRON MAN"] = (22, {})
card1.answers["BLACK PANTHER"] = (20, {}) 
card1.answers["THE HULK"] = (12, {})
card1.answers["THOR"] = (12, {})
card1.answers["BLACK WIDOW"] = (6, {})
card1.answers["SPIDERMAN"] = (3, {})
card1.answers["HAWKEYE"] = (3, {})

# Card 3

card2 = GameCard("Name a Common Candy Bar Component")
card2.answers["CHOCOLATE"] = (36, {})
card2.answers["PEANUTS"] = (22, {})
card2.answers["CARAMEL"] = (15, {}) 
card2.answers["ALMONDS"] = (12, {})
card2.answers["NOUGAT"] = (10, {})
card2.answers["COCONUT"] = (5, {})

# Card 4

card3 = GameCard("Name a Type of Insurance")
card3.answers["CAR"] = (31, {})
card3.answers["HEALTH"] = (27, {})
card3.answers["LIFE"] = (20, {}) 
card3.answers["HOME"] = (10, {})
card3.answers["FLOOD"] = (6, {})
card3.answers["TRAVEL"] = (4, {})
card3.answers["BLACKJACK"] = (2, {})

# Card 5

card4 = GameCard("Where Do Kids Nowadays Spend Most of their Time?")
card4.answers["ROOM"] = (28, {})
card4.answers["SCHOOL"] = (22, {})
card4.answers["INTERNET"] = (16, {}) 
card4.answers["MALL"] = (12, {})
card4.answers["FRIEND'S HOUSE"] = (10, {})
card4.answers["PARK"] = (8, {})
card4.answers["WORK"] = (4, {})

# Card 6

card5 = GameCard("Name A Fruit You Might Eat In The Morning")
card5.answers["BANANA"] = (25, {})
card5.answers["GRAPE FRUIT"] = (22, {})
card5.answers["STRAWBERRY"] = (19, {}) 
card5.answers["APPLE"] = (15, {})
card5.answers["ORANGE"] = (12, {})
card5.answers["MELON"] = (5, {})
card5.answers["PEACH"] = (2, {})

# Card 7

card6 = GameCard("Name A Country With A Lot of Land")
card6.answers["RUSSIA"] = (31, {})
card6.answers["CHINA"] = (17, {})
card6.answers["CANADA"] = (17, {}) 
card6.answers["USA"] = (16, {})
card6.answers["GREENLAND"] = (5, {})
card6.answers["MEXICO"] = (4, {})
card6.answers["AUSTRALIA"] = (4, {})
card6.answers["INDIA"] = (2, {})
'''

# A list of cards to help replicate generating random cards.
list_of_cards = classes.cards

# This list just contains a list of the answers in order to print said answers instead of using the dictionary.
list_of_answers = []

class Game:
    
    # Constructor to create the game that takes two Team objects as arguments 
    def __init__(self, first_team_arg, second_team_arg):
        self.first_team = first_team_arg
        self.second_team = second_team_arg
        self.is_running = True
        self.temp_score = 0
        self.missed_answers = 0
        self.round = 0
        self.board = Board()

    # Function to toggle to the current team based on the current round
    def get_current_team(self):
        players = [self.first_team, self.second_team]
        return players[self.round % len(players)]

    # Function to toggle to the next team based on the current round
    def get_next_team(self):
        players = [self.first_team, self.second_team]
        return players[(self.round + 1) % len(players)]

    # Function that clears the screen and shows all the game info on the screen 
    def refresh_screen(self, duration=1.5):
        self.clear_screen()
        sleep(duration)
        print(f"Round {self.round + 1}")
        print(f"Round Score: {self.temp_score}")
        print(f"{self.first_team.name}'s Score: {self.first_team.score} | {self.second_team.name}'s Score: {self.second_team.score}")
        self.board.print_board()
    
    def clear_screen(self):
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    def score_limit(self):
        if self.first_team.score >= 300 or self.second_team.score >= 300:
            return True
        else:
            return False

    # Returns whoever has the highest score
    def highest_score(self):
        if self.first_team.score > self.second_team.score:
            return self.first_team
        elif self.second_team.score > self.first_team.score:
            return self.second_team
        else:
            return "There was a tie!"

    # Main Play Function
    def play(self, first_team_arg, second_team_arg):

        self.first_team = first_team_arg
        self.second_team = second_team_arg

        while self.is_running:

            # for loops that does two rounds
            for x in range(2):

                # Pops a random card and makes it the current card
                current_card = list_of_cards.pop(random.randint(0, len(list_of_cards) - 1))

                # Clear the list_of_answers list for different rounds.
                # I might make this a variable in the constructor, honestly. 
                list_of_answers = []

                # Appends each answer to the list of answers. Note that the answers are the keys to the GameCard object's dictionary.
                for keys in current_card.answers:
                    list_of_answers.append(keys)

                # Counter to keep up with how many answers are not on the board
                counter = len(current_card.answers)

                # Clear the board, definitely helps for starting different rounds.
                self.board.clear_board()

                # Builds the board using the length of the number of answers.
                self.board.build_board(len(current_card.answers))

                # gets the current team and stores the current team in a variable to be used. 
                current_team = self.get_current_team()

                while counter != 0:

                    # Check to see if the playing team has ran out of guesses.
                    if self.missed_answers == 3:
                        print(f"Oops, you've guessed incorrectly three times! It's {self.get_next_team().name}'s turn!")
                        current_team = self.get_next_team() # Since the current play team missed three times, the current team is now the next team.
                        sleep(2)
                        break

                    self.refresh_screen()
                    print(current_card.question)
                    print(f"Number of Guesses Left: {3 - self.missed_answers}")
                    answer = input(f"{current_team.name}, What is your answer: ").upper()
                    print()
                    
                    for answers in dict.values(current_card.answers):
                        # Checks for similar answers
                        if answer in answers[1]:
                            for key, value in dict.items(current_card.answers):
                                if value == answers:
                                    answer = key.upper()
                                    break
                            break

                    if answer not in list_of_answers:
                        self.missed_answers += 1
                        print("Oops, wrong answer!")
                        sleep(2)
                    else:                  
                        print("You got it!")
                        index = list_of_answers.index(answer) # Gets the index of the answer from the list of answers and stores it.
                        self.board.board[index] = answer + " " + str(current_card.answers[answer][0]) # stores the answer with the score on the board given the index
                        counter -= 1
                        list_of_answers[index] = ""
                        self.temp_score += current_card.answers[answer][0] # take the score and add it to the temporary score variable
                        sleep(2)

                self.missed_answers = 0

                if counter != 0:
                    self.refresh_screen()
                    print(current_card.question)
                    answer = input(f"{current_team.name}, What is your answer: ").upper()

                    for answers in dict.values(current_card.answers):
                        # Checks for similar answers
                        if answer in answers[1]:
                            for key, value in dict.items(current_card.answers):
                                if value == answers:
                                    answer = key.upper()
                                    break
                            break

                    if answer in list_of_answers:
                        # If the answer is correct, like for the first team in the round, we just get the index,
                        # then store the answer with the score on the board using that index. 
                        # Then take the score and add it to the temporary score and give it to the stealing team.
                        # Then we just refresh the screen say they won and reset the temporary score.
                        index = list_of_answers.index(answer)
                        self.board.board[index] = answer + " " + str(current_card.answers[answer][0])
                        self.temp_score += current_card.answers[answer][0]
                        current_team.score += self.temp_score
                        self.refresh_screen()
                        print(f"{current_team.name} has won the round!")
                        self.temp_score = 0
                        self.round += 1
                        sleep(3)

                        if self.score_limit():
                            return self.highest_score()

                        continue
                # This part is for if the list_of_answers is empty or if the stealing team got the wrong answer.
                self.get_current_team().score += self.temp_score
                self.refresh_screen()
                print(f"{self.get_current_team().name} has won the round!")
                self.temp_score = 0
                self.round += 1

                if self.score_limit():
                    return self.highest_score()

                sleep(3)

            while True:
                answer = input("Do you want to continue playing? Press Y/y for continue and N/n to stop!").upper()
                if(answer == "Y"):
                    break
                elif(answer == "N"):
                    return self.highest_score()
                else:
                    print("Sorry, wrong input!") 