###############################################################################
"""
    This module holds the tic, tac, toe game.
"""
###############################################################################
import random
from tabulate import tabulate
board_file = "tttboard.txt"

# Tic, Tac, Toe board
board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]


def make_board():
    """ This function writes to an external file the game board."""
    with open(board_file, "w", encoding='utf-8') as file:
        file.write(tabulate(board_file, tablefmt = "fancy_grid"))


def print_board():
    '''Prints the updated board'''
    print(tabulate(board, tablefmt = "fancy_grid"))


def check_win(letter):
    ''' 
    This function checks if the letters "X" or "O" have won.
    '''
    # Horizontal win (rows)
    for row in board:
        if all(cell == letter for cell in row):
            print("Horizontal")
            return True
    # Vertical win (colums)
    for col in range(3):
        if all(board[row][col] == letter for row in range(3)):
            return True
        else:
            continue
    # Checking diagonal lines
    for col in range(3):
        if all(board[i][i] == letter for i in range(3)):
            print("Diagonal")
            return True
        if all(board[i][2-i] == letter for i in range(3)):
            print("Diagonal")
            return True
        return False


def tie():
    '''Check is the board is full, and game tied.'''
    return all(cell in ["X", "O"] for row in board for cell in row)


def reset_board():
    '''This function resets the board.'''
    global board
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]


def tic_tac_toe(opponent):
  '''
  Main game function. Includes the players input, the computer's turn,
  and calls tie or win functions.
  Opponent takes a random alive character, and plays as the computer.
  '''
  print(f"You are playing Tic, Tac, Toe {opponent.title()}! \nPick an available"
        + " number of your choice to place your mark.")
  while True:
    print("Your turn!")
    print_board()
    try:
        # player turn
        choice = int(input("What numbered square will you pick? "))
        if choice < 1 or choice > 9:
            print("Thats not a choice. Pick an available number on the board.")
            continue
        # Finding player choice input
        row, col = divmod(choice - 1, 3)
        if board[row][col]not in ["X", "O"]:
            board[row][col] = "X"
        else:
            print("That's not a choice. Pick an available"
                  + " number on the board.")
            continue
        if check_win("X"):
            print_board()
            print("You won!")
            reset_board()
            break
        # If opponent wins
        elif check_win("O"):
            print_board()
            print("You lost!")
            reset_board()
            break
        # Checking for tie
        elif tie():
            print_board()
            print("It is a tie!")
            reset_board()
            break
        # opponent turn
        empty_space = [(r, c) for r in range(3)
                       for c in range(3) if board [r][c] not in ["X", "O"]]
        if empty_space:
            random_space = random.choice(empty_space)
            board[random_space[0]][random_space[1]] = "O"
            print(f"{opponent.title()}'s turn:")
            print_board()
        # If player wins
        if check_win("X"):
            print_board()
            print("You won!")
            reset_board()
            break
        # If opponent wins
        elif check_win("O"):
            print_board()
            print("You lost!")
            reset_board()
            break
        # Checking for tie
        elif tie():
            print_board()
            print("It is a tie!")
            reset_board()
            break
    except ValueError:
        print("Invalid input. Pick an available number.")