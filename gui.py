import time

import PySimpleGUI as sg
from classes import Team
from game import Game
import game
import random

sg.theme('BlueMono')


def make_window1():
    """
    This is the first window that allows the users to interact with the game.
    Using this window, users can view instructions, start the game or add a new card.
    :return:
    """

    layout = [
        [sg.Image(r'family.PNG')],
        [sg.Text('Click the below buttons to interact with the game')],
        [sg.Button('View Instructions', key='-VIEW_INSTRUCTIONS-'),
         sg.Button('Play Game', key='-PLAY_GAME-'),
         sg.Button('Add Cards', key='-ADD_CARDS-')]]
    return sg.Window('Start Window', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window2():
    """
    This window is used to display the game instructions.
    :return:
    """
    layout = [
        [sg.Image(r'rules.PNG')],
        [sg.Button('Exit', key='-EXIT_INSTRUCTIONS-')]]

    return sg.Window('Rules', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window3():
    """
    Using this window, the user specifies the teams to be involved in the game.
    In other words, user specifies team names using this window.
    :return:
    """
    layout = [
        [sg.Image(r'team.PNG')],
        [sg.Text('Team 1 name: '), sg.Input(key='-TEAM1-', size=(20, 10))],
        [sg.Text('Team 2 name: '), sg.Input(key='-TEAM2-', size=(20, 10))],
        [sg.Text(size=(40, 1), key='-TEAM_INVALID-', text_color='red')],
        [sg.Button('Submit', key='-TEAM_INFO-')]]
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
    layout = [
        [sg.Image(r'family.PNG')],
        [sg.Text('This is a place holder for question',
                 key='-GAME_QUESTION-',
                 font=("Arial", 15),
                 text_color='#F07610')],
        [sg.Text('*** Score 0',
                 font=("Arial", 12),
                 key='-TEAM1_SCORE-',
                 size=(10, 1)),
         sg.Text('Round score: 0',
                 font=("Arial", 12),
                 key='-ROUNDSCORE-'),
         sg.Text('*** Score 0',
                 font=("Arial", 12),
                 key='-TEAM2_SCORE-',
                 size=(10, 1))],
        [sg.Text('*** have *** remaining tries',
                 key='-TRIAL-')]]
    if num_answer % 2 == 0:
        num_answer = num_answer // 2
    else:
        num_answer = (num_answer // 2)
        odd = True
    for ans in range(num_answer):
        layout.append([sg.Button(str(ans + 1),
                                 font=("Arial", 25),
                                 key='-HIDDEN_ANS' + str(ans + 1) + '-'),
                       sg.Button(str(ans + num_answer + 1),
                                 font=("Arial", 25),
                                 key='-HIDDEN_ANS' + str(ans + num_answer + 1) + '-')])

    if odd:
        layout.append([sg.Button(str(num_answer + num_answer + 1),
                                 font=("Arial", 25),
                                 key='-HIDDEN_ANS' + str(num_answer + num_answer + 1) + '-')])

    layout.append([sg.Text('Please enter your answer for the question')])
    layout.append([sg.Input(key='-QUESTION_ANS-', enable_events=True)])
    layout.append([sg.Button('Submit Answer', key='-GAME_ANSWER-')])

    return sg.Window('Main Game', layout, element_justification='center',
                     modal=True, finalize=True, grab_anywhere=True)


def make_window5():
    """
    This window is used to display the winner of the game after the game is over.
    Users can opt to continue with the game using this window.
    :return:
    """
    layout = [
        [sg.Image(r'game.PNG')],
        [sg.Text('The winner is'), sg.Text('****', key='-WINNER-')],
        [sg.Text('Do you want to play again?')],
        [sg.Button('YES', key='-CONTINUE_GAME-'), sg.Button('NO', key='-END_GAME-')]]

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
        [sg.Text('Enter question: '), sg.Input(key='-NEW_QUESTION-', size=(20, 10))],
        [sg.Text('How many answers do you want to put? (4-8 answers only)'),
         sg.Input(key='-ANSWER_NUMBER-', size=(10, 10))],
        [sg.Button('Submit Card', key='-QUESTION_SUBMITTED-')]]
    return sg.Window('Add Card', layout, element_justification='center',
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
    layout.append([sg.Button('Submit Answers', key='-ANSWER_SCORE-')])

    return sg.Window('Add Card', layout, element_justification='center',
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

    elif event == '-EXIT_INSTRUCTIONS-':
        window2.close()
    elif event == '-PLAY_GAME-':
        window3 = make_window3()
    elif event == '-GAME_ANSWER-':

        answer = values['-QUESTION_ANS-']
        list_of_answers = []
        game_round = 1
        steal = False
        print(game_instance.round)

        for keys in current_card.answers:
            list_of_answers.append(keys)

        window4['-QUESTION_ANS-'].update('')

        if answer.upper() not in list_of_answers:

            game_instance.missed_answers += 1
            window4['-TRIAL-'].update(f'{current_team.name} have {3 - game_instance.missed_answers} remaining tries')

            if game_instance.missed_answers == 1:
                random_window = wrong_ans(1)
                random_window.bring_to_front()
                time.sleep(1)
                random_window.close()

            if game_instance.missed_answers == 2:
                random_window = wrong_ans(2)
                random_window.bring_to_front()
                time.sleep(1)
                random_window.close()
            if steal:
                game_round += 1
                game_instance.round += 1
                if current_team == first_team:
                    window4['-TEAM1_SCORE-'].update(f"{current_team.name}'s score: {game_instance.temp_score}")
                    game_instance.temp_score = 0
                elif current_team == second_team:
                    window4['-TEAM2_SCORE-'].update(f"{current_team.name}'s score: {game_instance.temp_score}")
                    game_instance.temp_score = 0

                current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))
                time.sleep(1)
                window4.close()
                window4 = make_window4(len(current_card.answers))
                window4['-GAME_QUESTION-'].update(f'{current_card.question}')
                window4['-TRIAL-'].update(f'{current_team.name} you got 3 guesses left!')
                window4['-ROUNDSCORE-'].update(f'Round score: 0')
                window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
                window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

        if game_instance.missed_answers == 3:

            game_instance.missed_answers = 0
            steal = True
            current_team = game_instance.get_next_team()
            random_window = wrong_ans(3)
            random_window.bring_to_front()
            time.sleep(1)
            random_window.close()
            window4['-TRIAL-'].update(f'{current_team.name} you got {3 - game_instance.missed_answers} guesses left!')

        elif answer.upper() in list_of_answers:

            index = list_of_answers.index(answer.upper())
            game_instance.temp_score += current_card.answers[answer.upper()][0]
            window4['-HIDDEN_ANS' + str(index + 1) + '-'].update(
                answer.upper() + " " + str(current_card.answers[answer.upper()][0]))
            window4['-ROUNDSCORE-'].update(f'Round score: {game_instance.temp_score}')

            if (index == len(list_of_answers) - 1) and (game_round == 2):

                time.sleep(1)
                window4.close()
                window5 = make_window5()
                window5['-WINNER-'].update(f'{current_team.name}')

            if index == len(list_of_answers) - 1:

                game_round += 1
                game_instance.round += 1
                current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))

                if current_team == first_team:
                    window4['-TEAM1_SCORE-'].update(f"{current_team.name}'s score: {game_instance.temp_score}")
                    game_instance.temp_score = 0
                elif current_team == second_team:
                    window4['-TEAM2_SCORE-'].update(f"{current_team.name}'s score: {game_instance.temp_score}")
                    game_instance.temp_score = 0

                time.sleep(2)
                window4.close()
                current_team = game_instance.get_next_team()
                window4 = make_window4(len(current_card.answers))
                window4['-GAME_QUESTION-'].update(f'{current_card.question}')
                window4['-TRIAL-'].update(f'{current_team.name} you got 3 guesses left!')
                window4['-ROUNDSCORE-'].update(f'Round score: 0')
                window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
                window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

            if steal:
                game_round += 1
                game_instance.round += 1
                if current_team == first_team:
                    window4['-TEAM1_SCORE-'].update(f"{current_team.name}'s score: {game_instance.temp_score}")
                    game_instance.temp_score = 0
                elif current_team == second_team:
                    window4['-TEAM2_SCORE-'].update(f"{current_team.name}'s score: {game_instance.temp_score}")
                    game_instance.temp_score = 0

                current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))
                time.sleep(1)
                window4.close()
                window4 = make_window4(len(current_card.answers))
                window4['-GAME_QUESTION-'].update(f'{current_card.question}')
                window4['-TRIAL-'].update(f'{current_team.name} you got 3 guesses left!')
                window4['-ROUNDSCORE-'].update(f'Round score: 0')
                window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
                window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

    elif event == '-TEAM_INFO-':
        if (values['-TEAM1-'] != '') and values['-TEAM2-'] != '':

            first_team = Team(values['-TEAM1-'])
            second_team = Team(values['-TEAM2-'])
            game_instance = Game(first_team, second_team)

            current_card = game.list_of_cards.pop(random.randint(0, len(game.list_of_cards) - 1))
            current_team = game_instance.get_current_team()

            window3.close()
            window4 = make_window4(len(current_card.answers))

            window4['-GAME_QUESTION-'].update(f'{current_card.question}')
            window4['-TRIAL-'].update(f'{current_team.name} you got 3 guesses left!')
            window4['-TEAM1_SCORE-'].update(f"{first_team.name}'s score: {first_team.score}")
            window4['-TEAM2_SCORE-'].update(f"{second_team.name}'s score: {second_team.score}")

        else:
            window3['-TEAM_INVALID-'].update('          Please fill both fields!')    
    elif event == '-ADD_CARDS-':
        window6 = make_window6()
    elif event == '-QUESTION_SUBMITTED-':
        window6.close()
        window7 = make_window7()
    elif event == '-ANSWER_SCORE-':
        window7.close()
    elif event == '-CONTINUE_GAME-':
        window5.close()
        window3 = make_window3()
    elif event == '-END_GAME-':
        break

window.close()

