import classes
from sqlite_db import intial_data, create_tables,\
    fetch_all


def familyfeud_database():
    
    try:
        create_tables()
        intial_data()
        fetch_all()

    except:
        fetch_all()

# A list of cards to help replicate generating random cards.
familyfeud_database()
list_of_cards = classes.cards

# This list just contains a list of the answers in order to print said answers instead of using the dictionary.
list_of_answers = []

def add_card(question, list_of_answers):

        card = classes.GameCard(question)

        for ans_list in list_of_answers:
            ans_list[0] = ans_list[0].upper()
            all_answers = ans_list[0].split("/")
            set_of_similar_answers = set()
            
            if(len(all_answers) > 1):
                set_of_similar_answers = set(all_answers[1:])
            
            card.answers[all_answers[0].upper()] = (ans_list[1], set_of_similar_answers)

class Game:
    
    # Constructor to create the game that takes two Team objects as arguments 
    def __init__(self, first_team_arg, second_team_arg):
        self.first_team = first_team_arg
        self.second_team = second_team_arg
        self.temp_score = 0
        self.missed_answers = 0
        self.round = 0
        self.similar_answer = False

    # Function to toggle to the current team based on the current round
    def get_current_team(self):
        players = [self.first_team, self.second_team]
        return players[self.round % len(players)]

    # Function to toggle to the next team based on the current round
    def get_next_team(self):
        players = [self.first_team, self.second_team]
        return players[(self.round + 1) % len(players)]

    # Returns whoever has the highest score
    def highest_score(self):
        if self.first_team.score > self.second_team.score:
            return self.first_team
        elif self.second_team.score > self.first_team.score:
            return self.second_team
        else:
            return "There was a tie!"

    def is_similar_answer(self, answer, card):
        for key, value in dict.items(card.answers):
            if answer.upper() in value[1]:
                self.similar_answer = True
                return key
        self.similar_answer = False
        return answer