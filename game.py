is_running = True
temp_score = 0
first_team_score = 0
second_time_score = 0
missed_answers = 0
current_team = ""
answer = ""

card0 = GameCard("In Horror Movies, Name a Place Teenagers Go Where There’s Always a Killer On the Loose")
card0.answers["Cabin"] = (49, ("Camp", "Woods"))
card0.answers["Graveyard"] = (12, ())
card0.answers["Movie Theatre"] = (6, ("Drive-In"))
card0.answers["Basement"] = (6, ("Cellar"))
card0.answers["Closet"] = (5, ())
card0.answers["Bathroom"] = (4, ("Shower"))
card0.answers["Bedroom"] = (4, ("Bed"))
card0.answers["Party"] = (4, ())

first_team_name = input("Team 1, Enter your name here: ")
second_team_name = input("Team 2, Enter your name here: ")

while is_running:
    # print the number of questions on screen
    # display the first question

    for x in range(2):
        while there are any answers still on the board:
            answer = input(f"{current_team}, What is your answer: ")

            if missed_answers == 3:
                print("Oops, you've guessed incorrectly three times!")
                break
            elif answer != ????????:
                missed_answers += 1
                print("Oops, wrong answer!")
            else:
                # show answer
                # add the answer points to the score total
        
        missed_answers = 0
        if the board is not empty:
            answer = input(f"{current_team}, What is your answer: ")

            if answer:
                # assign score to opposing team
                temp_score = 0
            else:
                # assign score to current team
                temp_score = 0
        
    print("Do you want to play two more rounds? ")

######

# Have a list variable that contains the list of cards to be added to the game
list_of_cards = []
​
#   GameCard class
#   Each card has a question (string) and a dictionary of answers
#   The key of the dictionary is the answer itself and the value is a set
# that contains the answer score in the first index and a set of possible
# synoynms (or 'close enough' answers).
class GameCard:
​
    def __init__(self, question):
        self.question = question
        self.answers = {}

'''   
# Card 0
card0 =  GameCard("Name a fruit.")
card0.answers["apple"] = (24, ("green apple", "red apple"))
​
# Card 1
​
card1 =  GameCard("Name a fruit.")
card1.answers["orange"] = (12, ("green apple", "red apple"))
​
# Card 2
​
card2 =  GameCard("Name a fruit.")
card2.answers["banana"] = (48, ("green apple", "red apple"))
​
list_of_cards.append(card0)
list_of_cards.append(card1)
list_of_cards.append(card2)
​

print(f"The question is: {card.question}")
​
for keys in card.answers:
    print(f"answer: {keys}  score: {card.answers[keys][0]}")
    
if "greenapple" in card.answers[keys][1]:
    print(True)
else:
    print(False)
 
​
print(list_of_cards)
'''     