import re
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def is_valid_marker(ch):
    return (bool(re.search(r'\S', ch))) and len(ch) == 1

def is_valid_marker_and_not_same_character_as_p1(ch2, ch1):
    return (bool(re.search(r'\S', ch2))) and (ch2 != ch1) and (len(ch2) == 1)

def print_board(board):
    for row in board:
        print("|", " | ".join(row), "|")

def make_move(marker, row, column, board):
    row = check_and_convert(row, len(board[0]))
    column = check_and_convert(column, len(board[0]))
    board[row][column] = marker

def check_and_convert(str, size):
    # Check if the string is a digit and if it is between 0 and 3
    if str.isdigit() and 0 <= int(str) < size:
        return int(str)  # Convert the string to an integer and return it
    else:
        return None
def check_game_win(board):
    # Check rows
    for row in board:
        if all(cell == row[0] and cell != '' for cell in row):  # Check if all cells in this row are the same and not empty
            return True

    # Check columns
    for col in range(len(board[0])):  # Iterate over each column
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(len(board))):  # Check if all cells in this column are the same and not empty
            return True

    # Check left-to-right diagonal
    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(len(board))):  # Check the diagonal from top-left to bottom-right
        return True

    # Check right-to-left diagonal
    if all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] and board[i][len(board) - 1 - i] != '' for i in range(len(board))):  # Check the diagonal from top-right to bottom-left
        return True

    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    play_flaq = "N";
    play_flag = input("Do you want to play Tic Tac Toe? Answer Y or N: ")
    p1Marker = "X"
    p2Marker = "O"
    while play_flag == "Y":
        p1Marker = input("Pick any character save for white spaces for player 1: ")
        while(not is_valid_marker(p1Marker)):
            p1Marker = input("Character is invalid, pick any character save for white spaces for player 1: ")
        p2Marker = input("Pick any character save for white spaces for player 2: ")
        while(not is_valid_marker_and_not_same_character_as_p1(p2Marker, p1Marker)):
            p1Marker = input("Character is invalid, pick any character save for white spaces for player 2: ")
        play_flag = "N"
        print_board(board)
        while(not check_game_win(board)):
            row = input("Player 1 please make your move, pick row ")
            column = input("Player 1 please make your move, pick column ")
            make_move(p1Marker, row,column, board)
            print_board(board)
            row = input("Player 2 please make your move, pick row ")
            column = input("Player 2 please make your move, pick column ")
            make_move(p2Marker, row,column, board)
            print_board(board)
        play_flag = input("Do you want to play Tic Tac Toe? Answer Y or N: ")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
