# --------- Global Variables ---------

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a Position from 1 - 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a Position from 1 - 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    # Check Rows
    row_winner = check_rows()
    # Check Columns
    column_winner = check_columns()
    # Check Dioganals
    dioganal_winner = check_dioganals()

    if row_winner:
        # There is a Winner
        winner = row_winner
    elif column_winner:
        # There is a Winner
        winner = column_winner
    elif dioganal_winner:
        # There is a Winner
        winner = dioganal_winner
    else:
        # There is no winner
        winner = None


    

def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

def check_dioganals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[3]

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False    

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()


# Board
# Display Game
# Play Game
# Handle Turn
# Check Win
#     Check Rows
#     Check Columns
#     Check Dioganals
# Check Tie
# Filp Player
