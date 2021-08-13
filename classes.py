# Variable that contains all the cards for the game
# A card is automatically added to this list when it is created
cards = []

class GameCard:
    def __init__(self, question):
        self.question = question
        self.answers = {}
        cards.append(self)

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

