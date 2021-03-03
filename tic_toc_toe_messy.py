# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def draw_board(board):
    """This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board 
    (ignore index 0)"""

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


def inputPlayerLetter():
    """Lets the player type which letter they want to be.
       Returns a list with the player’s letter as the first item, 
       and the computer's letter as the second."""

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']


def whoGoesFirst():
    """Randomly choose the player who goes first."""

    return "computer" if random.randint(0,1) == 0 else "player"


def playAgain():
    """This function returns True if the player wants to play again, otherwise it returns False."""

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter

def winner(bo, le):
    """Given a board and a player’s letter, this function returns True if that player has won.
       We use bo instead of board and le instead of letter so we don’t have to type as much."""

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    # TODO: Fix the indentation of this lines and the following ones.
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def copy_board(board):
    """Make a duplicate of the board list and return it the duplicate."""

    dupeBoard = []
    length_of_board = len(board)
    
    for i in range(length_of_board):  # TODO: Clean this mess!
        dupeBoard.append(board[i])
    return dupeBoard

def is_space_free(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def getPlayerMove(board):
    """Let the player type in their move."""

    player_move = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def chooseRandomMoveFromList(board, movesList):
    """Returns a valid move from the passed list on the passed board.
       Returns None if there is no valid move."""

    possibleMoves = []
    for move in movesList:
        if is_space_free(board, move):
            possibleMoves.append(move)

    if len(possibleMoves) != 0: # TODO: How would you write this pythanically? (You can google for it!)
        return random.choice(possibleMoves)
        #The else statement is not necessary.
    return None

def getComputerMove(board, AILetter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """Given a board and the computer's letter, determine where to move and return that move."""

    #Changed computerLetter to AILetter
    if AILetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for move in range(1, size_of_board):
        copy = copy_board(board)
        if is_space_free(copy, move):
            makeMove(copy, AILetter, move)
            if winner(copy, AILetter):
                return move

    # Check if the player could win on their next move, and block them.
    for i in range(1, size_of_board):
        copy = copy_board(board)
        if is_space_free(copy, i):
            makeMove(copy, playerLetter, i)
            if winner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def board_is_full(board):
    """Return True if every space on the board has been taken. Otherwise return False."""

    for i in range(1, size_of_board):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')
# TODO: Break down code block into smaller methods. Use TODO's and the 
        # comment above each section as a guide 
        # for refactoring.
size_of_board = 10

while True:
    theBoard = [' '] * size_of_board # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    playerLetter, AILetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    
    """Removed flag variable""" # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                                #       See whether you can get rid of this 'flag' variable. If so, remove it.

    while True: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                         #       Use a meaningful name for the function you choose.
        if turn == 'player':
            # Player’s turn.
            draw_board(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                draw_board(theBoard)
                print('Hooray! You have won the game!')
                break

                #else not necessary

            if board_is_full(theBoard):
                draw_board(theBoard)
                print('The game is a tie!')
                break

             #else not necessary

            turn = 'computer'


        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, AILetter)
            makeMove(theBoard, AILetter, move)

            if winner(theBoard, AILetter):
                draw_board(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False

                 #else is not necessary

            if board_is_full(theBoard):
                draw_board(theBoard)
                print('The game is a tie!')
                break

                #else is not necessary we can just unindent "turn" below
            turn = 'player'

    if not playAgain():
        break