import time

import PySimpleGUI as sg
import classes
from classes import Team
from game import Game
import game
import random
from addcards import add_card
from sqlite3 import Error
#from database_file import add_card_to_db, sqlite3_connection

sg.theme('BlueMono')


def make_window1():
    """
    This is the first window that allows the users to interact with the game.
    Using this window, users can view instructions, start the game or add a new card.
    :return:
    """

    layout = [
        [sg.Image(r'family.PNG')],
        [sg.Text('Click the buttons below to interact with the game')],
        [sg.Button('View Instructions', key='-VIEW_INSTRUCTIONS-', mouseover_colors='green'),
         sg.Button('Play Game', key='-PLAY_GAME-', mouseover_colors='green'),
         sg.Button('Add Cards', key='-ADD_CARDS-', mouseover_colors='green')]]
    return sg.Window('Welcome to Family Feud', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window2():
    """
    This window is used to display the game instructions.
    :return:
    """
    layout = [
        [sg.Image(r'rules.PNG')],
        [sg.Button('Exit', key='-EXIT_INSTRUCTIONS-', mouseover_colors='green')]]

    return sg.Window('Game rules', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window3():
    """
    Using this window, the user specifies the teams to be involved in the game.
    In other words, user specifies team names using this window.
    :return:
    """
    layout = [
        [sg.Image(r'team.PNG')],
        [sg.Text('Enter team1 name: '), sg.Input(key='-TEAM1-', size=(20, 10))],
        [sg.Text('Enter team2 name: '), sg.Input(key='-TEAM2-', size=(20, 10))],
        [sg.Text(size=(40, 1), key='-TEAM_INVALID-', text_color='red')],
        [sg.Button('Submit', key='-TEAM_INFO-', mouseover_colors='green')]]
    return sg.Window('Team Info', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window4(num_answer=3):
    """
    This is window will be used by the user to play the game.
    Using this window, user will be able to guess the answers displayed on the board.
    :param num_answer:
    :return:
    """

    odd = False
    buttons_left = []
    buttons_right = []
    layout = [
        [sg.Image(r'family.PNG')],
        [sg.Text(key='-GAME_QUESTION-',
                 font=("Arial", 15),
                 text_color='#F07610',
                 size=(30, None),
                 justification='center')],
        [sg.Text('*** Score 0',
                 font=("Arial", 12),
                 key='-TEAM1_SCORE-',
                 size=(None, 1),
                 justification='right'),
         sg.Text('Round score: 0',
                 font=("Arial", 12),
                 key='-ROUNDSCORE-',
                 size=(None, 1),
                 justification='center'),
         sg.Text('*** Score 0',
                 font=("Arial", 12),
                 key='-TEAM2_SCORE-',
                 size=(None, 1),
                 justification='left')],
        [sg.Text('*** have *** remaining tries',
                 key='-TRIAL-',
                 size=(None, 1),
                 justification='center')]]
    if num_answer % 2 == 0:
        num_answer = num_answer // 2
    else:
        num_answer = (num_answer // 2)
        odd = True
    for gui_ans in range(num_answer):

        buttons_left.append([sg.Button(str(gui_ans + 1),
                                       font=("Arial", 15),
                                       key='-HIDDEN_ANS' + str(gui_ans + 1) + '-',
                                       button_color='#07125B')])

        buttons_right.append([sg.Button(str(gui_ans + num_answer + 1),
                                        font=("Arial", 15),
                                        key='-HIDDEN_ANS' + str(gui_ans + num_answer + 1) + '-',
                                        button_color='#07125B')])

    if odd:
        buttons_right.append([sg.Button(str(num_answer + num_answer + 1),
                                        font=("Arial", 15),
                                        key='-HIDDEN_ANS' + str(num_answer + num_answer + 1) + '-',
                                        button_color='#07125B')])

    layout.append([sg.Column(buttons_left, element_justification='right'),
                  sg.Column(buttons_right, element_justification='left')])
    layout.append([sg.Text('Please enter your answer for the question')])
    layout.append([sg.Input(key='-QUESTION_ANS-', enable_events=True)])
    layout.append([sg.Text('', key='-ANSWER_PRESENT-', text_color='red', size=(None, 1))])
    layout.append([sg.Button('Submit Answer', key='-GAME_ANSWER-', mouseover_colors='green')])

    return sg.Window("Let's play", layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window5():
    """
    This window is used to display the winner of the game after the game is over.
    Users can opt to continue with the game using this window.
    :return:
    """
    layout = [
        [sg.Image(r'game.PNG')],
        [sg.Text('The winner is ****', size=(15, 1), key='-WINNER-')],
        [sg.Text('Do you want to play again?')],
        [sg.Text('', key='-NO_CARDS-', size=(None, 1), text_color='#F07610')],
        [sg.Button('YES', key='-CONTINUE_GAME-', mouseover_colors='green'),
         sg.Button('NO', key='-END_GAME-', mouseover_colors='green')]]

    return sg.Window('Game Over', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window6():
    """
    This window is used to add a new card.
    In other words, users can use this window to enter the question and number of answers for the question
    :return:
    """
    layout = [
        [sg.Image(r'card.PNG')],
        [sg.Text("Please enter question (can't be empty): "), sg.Input(key='-NEW_QUESTION-', size=(20, 10))],
        [sg.Text('How many answers do you want to put? (4-8 answers only)'),
         sg.Input(key='-ANSWER_NUMBER-', size=(10, 10))],
        [sg.Text('', size=(20, 1), key='-INVALID_WINDOW6-', text_color='red')],
        [sg.Button('Submit Card', key='-QUESTION_SUBMITTED-', mouseover_colors='green')]]
    return sg.Window('Submit question', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


"""
answer,score=input('Enter an answer followed by the corresponding score').spilt
for i in answers(1,key):
    [[sg.Text('Answer:')], sg.Input(key='-ANSWERANDSCORE-', size=(20,20))]
except ValueError:
    print('Invalid Input. Try again.')
"""


def make_window7(num=4):
    """
    This window is used to enter answers and scores for the question that was submitted by make_window6()
    :param num:
    :return:
    """
    layout = [[sg.Image(r'card.PNG')]]

    for i in range(num):
        layout.append([sg.Text('Answer ' + str(i + 1)),
                       sg.Input(size=(10, 10), key='-SUBMITTED_ANSWER' + str(i + 1) + '-'),
                       sg.Text('Score for answer ' + str(i + 1)),
                       sg.Input(size=(10, 10), key='-SUBMITTED_SCORE' + str(i + 1) + '-')])

    layout.append([sg.Text('', key='-INVALID_WINDOW7-', text_color='red', size=(20, 1))])
    layout.append([sg.Button('Submit Answers', key='-ANSWER_SCORE-')])

    return sg.Window('Submit answers', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def wrong_ans(num_wrong):
    """
    This window will act as a popup when a user enters a wrong answer.
    :param num_wrong:
    :return:
    """
    if num_wrong == 1:
        layout = [
            [sg.Button('X', font=("Arial", 30), button_color='red')]
        ]
    elif num_wrong == 2:
        layout = [
            [sg.Button('X', font=("Arial", 30), button_color='red'),
             sg.Button('X', font=("Arial", 30), button_color='red')]
        ]
    else:
        layout = [
            [sg.Button('X', font=("Arial", 30), button_color='red'),
             sg.Button('X', font=("Arial", 30), button_color='red'),
             sg.Button('X', font=("Arial", 30), button_color='red')]
        ]
    return sg.Window("", layout, element_justification='center',
                     finalize=True, background_color='white', no_titlebar=True)


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
        elif event == '-VIEW_INSTRUCTIONS-':

            window2 = make_window2()
            print(len(classes.cards))

        elif event == '-EXIT_INSTRUCTIONS-':

            window2.close()

        elif event == '-PLAY_GAME-':

            window3 = make_window3()

        elif event == '-GAME_ANSWER-':

            answer = values['-QUESTION_ANS-'].strip()

            window4['-QUESTION_ANS-'].update('')

            if (answer.upper() not in list_of_answers) and (steal is False):

                print("{0} Hahaha incorrect answer".format(str(steal)))

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
                    print('steal changed ' + str(steal))
                    current_team = game_instance.get_next_team()
                    window4['-TRIAL-'].update(
                        f'{current_team.name} you got 1 guess to steal!')

            elif steal:

                if (answer.upper() in list_of_answers) and (answer.upper() not in answers_displayed):

                    print(f'We are stealing in round {game_instance.round} and answer correct ')
                    index = list_of_answers.index(answer.upper())
                    game_instance.temp_score += current_card.answers[answer.upper()][0]
                    window4[f'-HIDDEN_ANS{str(index + 1)}-'].update(
                        answer.upper() + " " + str(current_card.answers[answer.upper()][0]))
                    window4['-ROUNDSCORE-'].update(f'Round score: {game_instance.temp_score}')

                    if current_team == first_team:

                        current_team.score += game_instance.temp_score
                        window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {current_team.score}")

                    else:

                        current_team.score += game_instance.temp_score
                        window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {current_team.score}")

                if (answer.upper() not in list_of_answers) or (answer.upper() in answers_displayed):

                    print(f'We are stealing in round {game_instance.round} and answer incorrect ')

                    if current_team == first_team:

                        second_team.score += game_instance.temp_score
                        window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

                    else:

                        first_team.score += game_instance.temp_score
                        window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")

                if (game_instance.round % 2) == 0:

                    highest_score = game_instance.highest_score()
                    answers_displayed = set()
                    print(f'We are stealing in round  {game_instance.round}')

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

                    print("Just updating guis")
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

                print("game round changed")
                game_instance.round += 1
                steal = False
                game_instance.temp_score = 0
                num_of_correct_ans = 0

            elif answer.upper() in answers_displayed:

                game_instance.missed_answers += 1
                print(f'Missed answer so far {game_instance.missed_answers}')
                if game_instance.missed_answers == 3:

                    game_instance.missed_answers = 0
                    steal = True
                    print('steal changed ' + str(steal))
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

            elif (answer.upper() in list_of_answers) and (answer.upper() not in answers_displayed):

                print("Not final round ")
                num_of_correct_ans += 1
                answers_displayed.add(answer.upper())
                index = list_of_answers.index(answer.upper())
                game_instance.temp_score += current_card.answers[answer.upper()][0]

                window4['-ANSWER_PRESENT-'].update('')
                window4[f'-HIDDEN_ANS{str(index + 1)}-'].update(
                    answer.upper() + " " + str(current_card.answers[answer.upper()][0]))
                window4['-ROUNDSCORE-'].update(f'Round score: {game_instance.temp_score}')

                if num_of_correct_ans == len(list_of_answers):

                    num_of_correct_ans = 0
                    game_instance.missed_answers = 0
                    current_team.score += game_instance.temp_score

                    if (game_instance.round % 2) == 1:

                        print("Final round 1")
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

                        print("Final round 2")
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
            if (values['-TEAM1-'] != '') and values['-TEAM2-'] != '':

                steal = False
                added_card = False
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

        elif event == '-ADD_CARDS-':

            window6 = make_window6()

        elif event == '-QUESTION_SUBMITTED-':

            try:

                question = values['-NEW_QUESTION-']
                num_ans = int(values['-ANSWER_NUMBER-'])

                if question == '':

                    window6['-INVALID_WINDOW6-'].update("Question can't be empty !")
                    raise Exception


                elif (4 > num_ans) or (num_ans > 8):

                    window6['-INVALID_WINDOW6-'].update('Answers range incorrect !')
    
                    raise Exception   

                window6['-NEW_QUESTION-'].update('')
                window6['-ANSWER_NUMBER-'].update('')

            except ValueError:

                if question == '':

                    window6['-INVALID_WINDOW6-'].update('Please enter valid input !')

                else:

                    window6['-INVALID_WINDOW6-'].update('Please enter valid integer !')

                window6.refresh()
                time.sleep(1)
                window6['-INVALID_WINDOW6-'].update('')
            
            except Exception:

                window6.refresh()
                time.sleep(1)
                window6['-INVALID_WINDOW6-'].update('')
                window6['-NEW_QUESTION-'].update('')
                window6['-ANSWER_NUMBER-'].update('')

            else:

                window6.close()
                window7 = make_window7(num_ans)

        elif event == '-ANSWER_SCORE-':

            try:

                list_of_new_answers = []

                for ans in range(num_ans):

                    if values[f'-SUBMITTED_ANSWER{ans + 1}-'] == '':
                        raise NameError

                    temp_list = [values[f'-SUBMITTED_ANSWER{ans + 1}-'], int(values[f'-SUBMITTED_SCORE{ans + 1}-'])]
                    list_of_new_answers.append(temp_list)
                add_card(question, list_of_new_answers)

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

            else:

                window7.close()

                #conn = sqlite3_connection()
                #add_card_to_db(conn, question, list_of_new_answers)

        elif event == '-CONTINUE_GAME-':

            try:

                window3 = make_window3()
                window5.close()

            except ValueError:

                window5['-NO_CARDS'].update('Our fault ! Please add a card to continue 🥺')
                time.sleep(1)
                window5.close()

        elif event == '-END_GAME-':
            break

    window.close()


if __name__ == "__main__":

    gui_event_logic()