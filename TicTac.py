# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:42:06 2023

@author: r171

"""
def empty_board(board):
    board[1]='   '
    board[2]='   '
    board[3]='   '
    board[4]='   '
    board[5]='   '
    board[6]='   '
    board[7]='   '
    board[8]='   '
    board[9]='   '

from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def result_board1(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' - ' + board[2] + ' - ' + board[3])
    
def result_board2(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' - ' + board[5] + ' - ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def result_board3(board):
    clear_output()
    print(' ' + board[7] + ' - ' + board[8] + ' - ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def result_board4(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' '+' ^ ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' '+' ^ ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def result_board5(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' '+'   '+' ^ ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' '+'   '+' ^ ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def result_board6(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' '+'   '+'   '+'   '+'   '+' ^ ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' '+'   '+'   '+'   '+'   '+' ^ ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def result_board7(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print(' '+'   '+'   '+'   '+'   '+'   ')
    print(' ' + board[4] + ' \ ' + board[5] + ' | ' + board[6])
   # print(' '+'   '+'   '+'   '+'   '+' ^ ')
    print(' ' + board[1] + ' | ' + board[2] + ' \ ' + board[3])
    
def result_board8(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print(' '+'   '+'   '+'   '+'   '+'   ')
    print(' ' + board[4] + ' | ' + board[5] + ' / ' + board[6])
   # print(' '+'   '+'   '+'   '+'   '+' ^ ')
    print(' ' + board[1] + ' / ' + board[2] + ' | ' + board[3])

    
    
def player_input():
    import ctypes # An included library with Python install.
    
    marker=" "
    #keep asking player 1 to choos x or O
    while marker !='X' and marker !='O':
        
        marker= input('Player 1, choose X or O:')
        if marker !='X' and marker !='O':
            ctypes.windll.user32.MessageBoxW(0, "wrong input", "Alert", 1)
    player1=marker
    if player1 == 'X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    #winner of tac toe?
    
    #all rows and check to see if they all share the same marker?
    if(board[1]== mark and board[2]==mark and board[3]==mark):
        result_board1(board)  
        return True
             
    elif(board[4]== mark and board[5]==mark and board[6]==mark):
        result_board2(board)  
        return True
    elif(board[6]== mark and board[7]==mark and board[9]==mark):
        result_board3(board)  
        return True
    elif(board[7] == mark and board[4] == mark and board[1] == mark):
        result_board4(board)  
        return True# down the middle
    elif(board[8] == mark and board[5] == mark and board[2] == mark):
        result_board5(board)  
        return True# down the middle
    elif(board[9] == mark and board[6] == mark and board[3] == mark):
        # down the right side
        result_board6(board)  
        return True
    elif(board[7] == mark and board[5] == mark and board[3] == mark):
        # diagonal
        result_board7(board)  
        return True
    elif(board[9] == mark and board[5] == mark and board[1] == mark):
    # diagonal
        result_board8(board)  
        return True
    else:
        return False
    #all columns, check to see if marker matches

    #2 diagonals check to see match
    
    
    
    
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    x=board[position]==' '
    
    return x
    



  
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    #board is full no space
    return True

def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = input('Choose your next position: (1-9) ')
    return int(position)
        


def replay():
    choice=input("play again??(Y/N)")
    return choice=='Y'

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    #empty_board(theBoard)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            
            display_board(theBoard)
            print("player1's turn")
            position = player_choice(theBoard)
            
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                #result_board(theBoard)
                print('player 1 Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                    game_on=False
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            print("Player 2's turn")
            position = player_choice(theBoard)
         
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                #result_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break