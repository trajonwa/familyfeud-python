import classes
from classes import GameCard


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