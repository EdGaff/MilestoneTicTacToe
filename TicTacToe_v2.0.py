# TicTacToe Game
# Home assignment from Bootcamp Python - Udemy
# Created in Jan/2018 by Mr. Gaff
__author__ = 'EdGaff'

import random


def print_board(board):
    """ Print out the selected board. """
    print(str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print(str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print(str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))


def players_turn():
    """ Return a random int, numbers 1 or 2. """
    return random.randint(1, 2)


def input_position(board):
    """ User inputs position, it's checked and returns the chosen position as int. """
    print_board(board)
    position = input('Choose a position: ')
    while position not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
        print('Your input must be a position from the matrix above.\n')
        position = input('Choose again: ')
    return int(position)


def check_position(board, position, turn):
    """ Check if the chosen position isn't already taken.
        Input the player's tag into the position and returns board[]. """
    board_position = board[position]
    while board_position == 'o' or board_position == 'x':
        print('Sorry, that position is already taken. Choose another one.\n')
        position = input_position(board)
        board_position = board[position]
    if turn == 1:
        board[position] = 'x'
        return board
    else:
        board[position] = 'o'
        return board


def get_board_position(p1name, p2name, board):
    """ Uses the other functions to receive input from users
        and checks for a win repeatedly until the end of the game. """
    rounds = 0
    turn = players_turn()
    while rounds < 9:
        if turn == 1:
            print('\n' + p1name + ', its your turn.\n')
            position = input_position(board)
            board = check_position(board, position, turn)
            if win(board):
                print('Congratulations! You won!')
                break
            turn = 2
        else:
            print('\n' + p2name + ', its your turn.\n')
            position = input_position(board)
            board = check_position(board, position, turn)
            if win(board):
                print('Congratulations! You won!')
                break
            turn = 1
        rounds += 1
    if rounds == 9:
        print('Nobody won this time.')
    else:
        pass


def win(board):
    if board[0] == board[1] == board[2] \
            or board[3] == board[4] == board[5] \
            or board[6] == board[7] == board[8] \
            or board[0] == board[3] == board[6] \
            or board[1] == board[4] == board[7] \
            or board[2] == board[5] == board[8] \
            or board[0] == board[4] == board[8] \
            or board[6] == board[4] == board[2]:
        return True


# Welcoming players:

print("Welcome to TicTacToe Gaff's Game.\n")

# Game objective and explanations:

print('The game is played by two players. The objective is to complete a Line, Column or Diagonal.'
      '\nWho completes it first win!\n')

# Running:

print('So, lets begin.\n')
p1_name = input('Whats your name? ')
print(p1_name + ', you will use x.\n')

p2_name = input('Whats the other players name? ')
print(p1_name + ', you will use o.')

game_on = True
theBoard = [x for x in range(0, 9)]

# Loop if the game is on:

while game_on:
    get_board_position(p1_name, p2_name, theBoard)
    boolean = True
    while boolean:
        answer = input('Do you want to play again? Yes or No? ')
        if answer.lower() in ('yes', 'no'):
            boolean = False
        if answer == 'no':
            game_on = False
        else:
            theBoard = [x for x in range(0, 9)]
            game_on = True


# The game is over:

print('\nThanks for playing.')
