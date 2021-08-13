import PySimpleGUI as sg

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