# Tic-Tac-Toe Game

from os import system
from random import randint

# Lambda expression for clearing the output console in windows
clear = lambda: system('cls')

# Function that displays the board of game
def display_board(board):
    clear()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Function that takes position from user to update the board and returns it
def input_position(board):
    position = ''

    while position not in range(1, 10) or not check_space_at_position(board, position):
        position = int(input('Enter the position (1-9): '))

        if position not in range(1, 10):
            print('Invalid position! Please try again.')

        if not check_space_at_position(board, position):
            print('This place is already filled. Please choose another position.')

    return position

# Function that lets the user choose his/her mark for the game
def choose_marks():
    mark = ''

    while mark not in ('X', 'O'):
        mark = input('Player 1: Do you want to be X or O? ').upper()

        if mark == 'X':
            print('Player 2: You will be "O"')
            return ('X', 'O')
        else:
            print('Player 2: You will be "X"')
            return ('O', 'X')

# Fucntion that randomly selects which player gets first chance
def choose_first_chance():
    if randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function that updates the board after user's input of position
def update_board(board, mark, position):
    board[position] = mark
    display_board(board)

# Function that tells if a particular position is vacant or not
def check_space_at_position(board, position):
    return board[position] == ' '

# Function that checks if the board is completely filled or not
def check_unfilled_board(board):
    for mark in board:
        return mark == ' '

# Function that checks for the winner
def check_winner(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

# Function that asks if the players want to play more
def replay():
    return input('Do you want to play more? (Yes/No): ').lower().startswith('y')


print('Welcome to Tic-Tac-Toe !!!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = choose_marks()

    turn = choose_first_chance()

    while True:

        # Player 1's turn
        if turn == 'Player 1':
            display_board(theBoard)
            print("Player 1's turn")
            position = input_position(theBoard)

            update_board(theBoard, player1_marker, position)

            if check_winner(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won the game.')
                break
            else:
                if not check_unfilled_board(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        # Player 2's turn
        else:
            display_board(theBoard)
            print("Player 2's turn")
            position = input_position(theBoard)

            update_board(theBoard, player2_marker, position)

            if check_winner(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won the game.')
                break
            else:
                if not check_unfilled_board(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break