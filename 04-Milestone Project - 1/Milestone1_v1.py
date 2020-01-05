# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 01:47:07 2020

@author: logan
"""

import random

def display_board(board):
    print('\n'*100)
    print(board[7]+"|"+board[8]+"|"+board[9])
    print('-'+" "+'-'+" "+'-')
    print(board[4]+"|"+board[5]+"|"+board[6])
    print('-'+" "+'-'+" "+'-')
    print(board[1]+"|"+board[2]+"|"+board[3])

def player_input():
    while True:
        option = input('Player1, choose X or O: ')
        
        if option != "X" and option != "O":
            continue        
        elif option == "X":
            return ("X","O")
        else:
            return ("O","X")
        
def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def choose_first():
    r1 = random.randint(1, 2) 
    if r1 == 1:
        return False #int(False) == 0 => player1 first, player_mark[0]
    else: 
        return True #int(True) == 0 => player2 first, player_mark[1]
    
def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return board.count(' ') == 0

def player_choice(board):
    position = int(input('Choose your next position: (1-9) '))
    while position < 1 or position > 9:
        position = int(input('Out of range. Plz input number between 1~9: '))
    if not space_check(board, position):
        return position 
    
def replay():
    replay = input('Play again?(Y/N) ')
    return replay == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    player_mark = player_input()
    start = choose_first()
    print(f'Player{int(start)+1} start first')
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ready = input('Are you ready?:(Y/N) ')

    while True:
        display_board(board)
        
        #First Player's' Turn
        place_marker(board, player_mark[int(start)], player_choice(board))
        display_board(board)

        if win_check(board,player_mark[int(start)]) or full_board_check(board):
            break
        
        #Second Player's turn.

        place_marker(board, player_mark[int(not start)], player_choice(board))
        display_board(board)
        
        if win_check(board,player_mark[int(not start)]) or full_board_check(board):
            break

    print("Congratulations! You have won the game!")
        
    if not replay():
        break