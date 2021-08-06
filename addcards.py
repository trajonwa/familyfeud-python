# import databasefile

import os
import classes
from time import sleep, time

'''
This is the file that contains the function that adds cards (GameCard Object).
Three Options:
1. Add a Card
    - Asks the user for the card question, all the answers, their values, and similar answers for each answer if they exist.
    - Question: String
    - Answer: String
    - Score: Int
    - Similar Answers: Set of Strings
2. View All Cards
    - Displays all the card questions that are currently in the game. Even ones created by the user.
    - WILL ADD: Possibly give the user the option to select one of the cards and view all the answers for the card.
3. Go Back To Main Menu
    - Self-explanatory feature
'''
# Function to clear the screen
def clear_screen():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

# Function to add a new card to the game.
def add_card():
    while True:
        clear_screen()
        choice = input("Enter 1 to add a Card. Enter 2 to see all Cards. Enter 3 to Return to Main Menu: ")
        if choice == "1":

            clear_screen()
            while True:
                # Creates the Card object using the input question from the user
                # Asks user for the number of answers for this card, which will be used for the upcoming for loop)
                card = classes.GameCard(input("Enter Question: "))
                num_of_answers = int(input("How many answers? "))
                
                # Using the number of answers, we'll loop through the number of answers
                # asking for the answer itself, it's value, and any similar answers
                for number in range(num_of_answers):
                    set_of_similar_answers = set()
                    answer = input(f"What's answer #{number+1}: ").upper()
                    score = int(input("What's the score for this answer: "))

                    sim = input("Any similar answers? Enter Y/y for yes. Enter anything else to continue: ")
                    if sim.upper() == "Y":
                        num_of_sim = int(input("How many similar answers: "))

                        for simnumber in range (num_of_sim):
                            similar = input(f"What's similar answer #{simnumber+1}: ").upper()
                            set_of_similar_answers.add(similar)
                    
                    # Here, we create the key:value pair using the answer as the key, and tuple as the value, 
                    # with the score being the first item and the set of similar answers as the second value
                    # I used a tuple since you can access it using indexing.
                    card.answers[answer] = (score, set_of_similar_answers)
                
                # Here, we just print the card, and all the data for the card!
                print("Thank you for creating a card! Here's the card: ")
                print("Question: ")
                print(card.question)
                print()
                print("Answers: [Score : Similar Answers]")
                for answer in card.answers:
                    print(f"{answer} : [{card.answers[answer][0]} : {card.answers[answer][1]}]")

                input("Press anything to continue: ")
                break

        elif choice == "2":
            # Prints out all the questions/cards for the game.
            for card in classes.cards:
                print(card.question)

            input("Press anything to continue: ")
            clear_screen()
        elif choice == "3":
            return
        else:
            print("Wrong input")
            continue
            