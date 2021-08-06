cards = []

class Board:

    def __init__(self):
        self.board = []
        self.dict_of_answers = {}
    
    def fill_dict(self, list_of_answers):
        count = 1
        for answer in list_of_answers:
            self.dict_of_answers[answer] = count
            count += 1

    def build_board(self, num_of_answers):
        for i in range(num_of_answers):
            self.board.append([f"{i+1}"])

    def print_board(self):
        for row in self.board:
            print("[ " + "".join(row) + " ]")

    def clear_board(self):
        self.board = []

class GameCard:
    def __init__(self, question):
        self.question = question
        self.answers = {}
        cards.append(self)

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0