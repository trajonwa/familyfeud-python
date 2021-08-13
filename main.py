import time
import game
import random
import PySimpleGUI as sg
from gui import make_window1, make_window2, make_window3, make_window4,\
    make_window5, make_window6, make_window7, wrong_ans
from classes import Team
from game import Game
from sqlite_db import add_card_to_db
from sqlite3 import Error




def gui_event_logic():

    # start off with 1 window open
    window1, window2, window3, window4, \
        window5, window6, window7, window8 = make_window1(), None, None, None, None, None, None, None

    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:  # if closing win 2, mark as closed
                window2 = None
            elif window == window1:  # if closing win 1, exit program
                break
        elif event == '-VIEW_INSTRUCTIONS-': # If the view instructions button is clicked, instructions are displayed
            window2 = make_window2()
        elif event == '-EXIT_INSTRUCTIONS-':# Closes the instructions
            window2.close()
        elif event == '-PLAY_GAME-': # Creates teams window
            window3 = make_window3()
        elif event == '-GAME_ANSWER-':
            """
            This is the main game logic.
            Here, we have three main categories.
            1. What happens when the answer is correct
            2. What happens when the answer is incorrect
            3. What happens during the steal round

            Find comments below.
            """
            answer = values['-QUESTION_ANS-'].strip()
            temp_answer = answer
            answer = game_instance.is_similar_answer(answer, current_card).upper()
            window4['-QUESTION_ANS-'].update('')

            if (answer not in list_of_answers) and (steal is False):
                """
                If answer is wrong and we not in the steal round,
                show the user they enter a wrong answer by showing X on the  screen.
                The number of X's is dependent on how many answers they've gotten so far.
                Steal round intialized here as well and player change if X = 3.
                """
                game_instance.missed_answers += 1
                random_window = wrong_ans(game_instance.missed_answers)
                random_window.bring_to_front()
                time.sleep(1)
                random_window.close()
                window4['-TRIAL-'].update(
                    f'{current_team.name} you have {3 - game_instance.missed_answers} tries remaining !')

                if game_instance.missed_answers == 3:
                    game_instance.missed_answers = 0
                    steal = True
                    current_team = game_instance.get_next_team()
                    window4['-TRIAL-'].update(
                        f'{current_team.name} you got 1 guess to steal!')

            elif steal:
                """
                We check four things in the steal round as shown by the four if statements.

                1. The answer is correct where we display the correct answer on the board and assign 
                    points to the team that got the answer correct.
                2. The is incorrect where points round points are give to the opposing team.
                3. Also, steal could happen in the second round ((game_instance.round % 2) == 0)
                    Where we end the game and create a window to say who won the round.
                4. If we're in the first round ((game_instance.round % 2) == 1), we need to create a card to 
                    be used in the next round.

                We also change steal to False in this elif code block.
                """
                if (answer in list_of_answers) and (answer not in answers_displayed):
                    
                    if (game_instance.similar_answer):
                        sg.popup_auto_close(f"{temp_answer} is similar to {answer} on the board!",
                         no_titlebar=True, background_color='green', font=("Arial", 12))
                        answers_displayed.add(temp_answer.upper())

                    index = list_of_answers.index(answer)
                    game_instance.temp_score += current_card.answers[answer][0]
                    window4[f'-HIDDEN_ANS{str(index + 1)}-'].update(
                        answer + " " + str(current_card.answers[answer][0]))
                    window4['-ROUNDSCORE-'].update(f'Round score: {game_instance.temp_score}')

                    if current_team == first_team:
                        current_team.score += game_instance.temp_score
                        window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {current_team.score}")
                    else:
                        current_team.score += game_instance.temp_score
                        window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {current_team.score}")
                if (answer not in list_of_answers) or (answer in answers_displayed):

                    if current_team == first_team:
                        second_team.score += game_instance.temp_score
                        window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")
                    else:
                        first_team.score += game_instance.temp_score
                        window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")

                if (game_instance.round % 2) == 0:
                    highest_score = game_instance.highest_score()
                    answers_displayed = set()

                    if type(highest_score) is str:
                        window4.refresh()
                        time.sleep(1)
                        window4.close()
                        window5 = make_window5()
                        window5['-WINNER-'].update(f'There was a tie')
                    else:
                        window4.refresh()
                        time.sleep(1)
                        window4.close()
                        window5 = make_window5()
                        window5['-WINNER-'].update(f'The winner is {highest_score.name}')

                if (game_instance.round % 2) == 1:
                    answers_displayed = set()
                    current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))
                    list_of_answers = []

                    for keys in current_card.answers:
                        list_of_answers.append(keys)

                    window4.refresh()
                    time.sleep(1)
                    window4.close()
                    window4 = make_window4(len(current_card.answers))
                    window4['-ROUNDSCORE-'].update(f'Round score: 0')
                    window4['-GAME_QUESTION-'].update(f'{current_card.question}')
                    window4['-TRIAL-'].update(f'{current_team.name} you got {3 - game_instance.missed_answers} guesses left!')
                    window4['-ROUNDSCORE-'].update(f'Round score: 0')
                    window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
                    window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

                game_instance.round += 1
                steal = False
                game_instance.temp_score = 0
                num_of_correct_ans = 0

            elif answer in answers_displayed:
                """
                This code block ensures answers already on the board can't be given as answers through the game
                """
                game_instance.missed_answers += 1

                if game_instance.missed_answers == 3:
                    game_instance.missed_answers = 0
                    steal = True
                    current_team = game_instance.get_next_team()
                    window4['-TRIAL-'].update(
                        f'{current_team.name} you got 1 guess to steal!')
                else:

                    window4['-ANSWER_PRESENT-'].update('Sorry, that answer is on the board!')
                    window4.refresh()
                    time.sleep(1)
                    window4['-ANSWER_PRESENT-'].update('')
                    window4['-QUESTION_ANS-'].update('')
                    window4['-TRIAL-'].update(
                        f'{current_team.name} you have {3 - game_instance.missed_answers} remaining tries')

            elif (answer in list_of_answers) and (answer not in answers_displayed):
                """
                In the if statement, a few things are checked.
                1. We check for similar answers 
                2. Check if submitted answer is the answer for the last item on the board.
                    - If submitted answer isn't the final answer to be displayed, we just update the guis
                    - If submitted answer is the final answer, we have to check which round we are in
                        - If first round ((game_instance.round % 2) == 1), we assign score to repective teams 
                            and change card and team for second round
                        - If second round ((game_instance.round % 2) == 0), we check which team has highest 
                            score and end the game accordingly.

                    - Other variables such as game round are changed when we on final round.  
                """
                if (game_instance.similar_answer):
                        sg.popup_auto_close(f"{temp_answer} is similar to {answer.lower()} on the board!",
                         no_titlebar=True, background_color='green', font=("Arial", 12))
                        answers_displayed.add(temp_answer.upper())

                num_of_correct_ans += 1
                answers_displayed.add(answer)
                index = list_of_answers.index(answer)
                game_instance.temp_score += current_card.answers[answer][0]
                window4['-ANSWER_PRESENT-'].update('')
                window4[f'-HIDDEN_ANS{str(index + 1)}-'].update(
                    answer + " " + str(current_card.answers[answer][0]))
                window4['-ROUNDSCORE-'].update(f'Round score: {game_instance.temp_score}')

                if num_of_correct_ans == len(list_of_answers):
                    num_of_correct_ans = 0
                    game_instance.missed_answers = 0
                    current_team.score += game_instance.temp_score

                    if (game_instance.round % 2) == 1:
                        if current_team == first_team:
                            window4['-TEAM1_SCORE-'].update(f"{current_team.name}'s score: {first_team.score}")
                        elif current_team == second_team:
                            window4['-TEAM2_SCORE-'].update(f"{current_team.name}'s score: {second_team.score}")

                        current_team = game_instance.get_next_team()
                        current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))
                        game_instance.temp_score = 0
                        answers_displayed = set()
                        list_of_answers = []

                        for keys in current_card.answers:
                            list_of_answers.append(keys)

                        window4.refresh()
                        time.sleep(1)
                        window4.close()
                        window4 = make_window4(len(current_card.answers))
                        window4['-GAME_QUESTION-'].update(f'{current_card.question}')
                        window4['-TRIAL-'].update(f'{current_team.name} you got 3 guesses left!')
                        window4['-ROUNDSCORE-'].update(f'Round score: 0')
                        window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
                        window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

                    elif (game_instance.round % 2) == 0:
                        highest_score = game_instance.highest_score()
                        if type(highest_score) is str:
                            window4.refresh()
                            time.sleep(1)
                            window4.close()
                            window5 = make_window5()
                            window5['-WINNER-'].update(f'There was a tie')
                        else:

                            window4.refresh()
                            time.sleep(1)
                            window4.close()
                            window5 = make_window5()
                            window5['-WINNER-'].update(f'The winner is {highest_score.name}')
                    game_instance.round += 1

        elif event == '-TEAM_INFO-':
            """
            This event logic validates user input submitted and if correct,
            we start the game by intializing some important variables such as teams playing and 
            creating the game instance to use throughout the game to access the methods in this class.

            """
            if (values['-TEAM1-'] != '') and values['-TEAM2-'] != '':
                steal = False
                first_team = Team(values['-TEAM1-'])
                second_team = Team(values['-TEAM2-'])
                game_instance = Game(first_team, second_team)
                game_instance.round = 1
                current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))
                current_team = game_instance.get_current_team()
                list_of_answers = []
                num_of_correct_ans = 0
                answers_displayed = set()

                for keys in current_card.answers:
                    list_of_answers.append(keys)

                window3.close()
                window4 = make_window4(len(current_card.answers))
                window4['-GAME_QUESTION-'].update(f'{current_card.question}')
                window4['-TRIAL-'].update(f'{current_team.name} you got {3 - game_instance.missed_answers} guesses left!')
                window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
                window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")
            else:
                window3['-TEAM_INVALID-'].update('          Please fill both fields!')
                window3.refresh()
                time.sleep(1)
                window3['-TEAM_INVALID-'].update('')

        elif event == '-ADD_CARDS-': # Create a window for submitting questions if this button is clicked
            window6 = make_window6()
        elif event == '-QUESTION_SUBMITTED-': 
            """
            This is used to enter the question to be added to the game.
            The try except blocks are used for user input validation.
            Window for entering answers is created here based on num_ans entered by the user.

            """
            try:
                question = values['-NEW_QUESTION-']
                num_ans = int(values['-ANSWER_NUMBER-'])
                if question == '':
                    window6['-INVALID_WINDOW6-'].update("Question can't be empty !")
                    raise Exception
                elif (4 > num_ans) or (num_ans > 8):
                    window6['-INVALID_WINDOW6-'].update('Answers range incorrect !')
                    raise Exception 
            except ValueError:
                if question == '':
                    window6['-INVALID_WINDOW6-'].update('Please enter valid input !')
                else:
                    window6['-INVALID_WINDOW6-'].update('Please enter valid integer !')
                
                window6['-NEW_QUESTION-'].update('')
                window6['-ANSWER_NUMBER-'].update('')
                window6.refresh()
                time.sleep(1)
                window6['-INVALID_WINDOW6-'].update('')
            except Exception:
                window6['-NEW_QUESTION-'].update('')
                window6['-ANSWER_NUMBER-'].update('')
                window6.refresh()
                time.sleep(1)
                window6['-INVALID_WINDOW6-'].update('')
            else:
                window6.close()
                window7 = make_window7(num_ans)
        elif event == '-ANSWER_SCORE-':
            """
            This window is used to enter the answers for the game.
            First, we use try except blocks for user validation and if
            correct input is entered, we use the add_card function in game to enter new cards to the game
            the close the window.

            """
            try:
                list_of_new_answers = []
                for ans in range(num_ans):
                    if values[f'-SUBMITTED_ANSWER{ans + 1}-'] == '':
                        raise NameError
                    temp_list = [values[f'-SUBMITTED_ANSWER{ans + 1}-'], int(values[f'-SUBMITTED_SCORE{ans + 1}-'])]
                    list_of_new_answers.append(temp_list)
                add_card_to_db(question.strip().upper(), list_of_new_answers)
            except ValueError:
                for ans in range(num_ans):
                    window7[f'-SUBMITTED_ANSWER{ans + 1}-'].update('')
                    window7[f'-SUBMITTED_SCORE{ans + 1}-'].update('')

                window7['-INVALID_WINDOW7-'].update('Please enter valid integer !')
                window7.refresh()
                time.sleep(1)
                window7['-INVALID_WINDOW7-'].update('')
            except NameError:
                for ans in range(num_ans):
                    window7[f'-SUBMITTED_ANSWER{ans + 1}-'].update('')
                    window7[f'-SUBMITTED_SCORE{ans + 1}-'].update('')

                window7['-INVALID_WINDOW7-'].update("Answer can't be empty !")
                window7.refresh()
                time.sleep(1)
                window7['-INVALID_WINDOW7-'].update('')
            except Error:
                window7['-INVALID_WINDOW7-'].update('That question exists. Please choose a different one !')
                window7.refresh()
                time.sleep(1)
                window7.close()
                window6 = make_window6()
            else:
                window7.close()

        elif event == '-CONTINUE_GAME-': # Take user back to teams gui
                window3 = make_window3()
                window5.close()
        elif event == '-END_GAME-': # Exit out of the program
            break
    window.close()

if __name__ == "__main__":
    gui_event_logic()