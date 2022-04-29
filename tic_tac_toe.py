# board setup
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    print(
        f"{board[0][0]} | {board[0][1]} | {board[0][2]} \n"
        "---------\n"
        f"{board[1][0]} | {board[1][1]} | {board[1][2]} \n"
        "---------\n"
        f"{board[2][0]} | {board[2][1]} | {board[2][2]} \n"
    )


# inital functions
def player_turn(name, symbol):
    valid_spot = False
    while not valid_spot:
        # choose row
        valid_row = False
        while not valid_row:
            row_choice = int(input(f"{name}, choose a row to place your {symbol}: ")) -1
            if row_choice < 0 or row_choice > 2:
                print(f"Sorry {name}, that choice is not available! Please try again. ")
            else:
                valid_row = True

        # choose column
        valid_column = False
        while not valid_column:
            column_choice = int(input(f"{name}, choose a column to place your {symbol}: ")) -1
            if column_choice < 0 or column_choice > 2:
                print(f"Sorry {name}, that choice is not available! Please try again. ")
            else: 
                valid_column = True

        # place symbol at loaction
        if board[row_choice][column_choice] == " ":
            board[row_choice][column_choice] = symbol
            valid_spot = True
        else:
            print(f"Sorry {name}, that space is already occupied! Please try again. ")

def check_for_win():
    # check for row win
    for row in range(len(board)):
        if board[row][0] != " ":
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                    return True

    # check for column win
    for column in range(len(board)):
        column_values = []
        for row in range(len(board)):
            column_values.append(board[row][column])
        if column_values[0] != " ":
            if column_values[0] == column_values[1] and column_values[1] == column_values[2]:
                return True

    # check for diagonal win
    # left to right 
    if board[0][0] != " ":
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True 

    # right to left
    if board[0][2] != " ":
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True


# player info
player_one_name = input("Player 1, what is your name? ")
player_two_name = input("Player 2, what is your name? ")
current_player = player_one_name
current_symbol = "X"

print_board()


# game loop
turns = 0
win = False
while turns <9:
    # player turn
    player_turn(current_player, current_symbol)

    # update board
    print_board()

    # determine if win
    if check_for_win():
        print(f"Congratulations! {current_player} has won the game!")
        win = True
        break

    # switch players
    if current_player == player_one_name:
        current_player = player_two_name
        current_symbol = "O"
    else:
        current_player = player_one_name
        current_symbol ="X"

    # update number of turns
    turns += 1

if not win:
    print("Oh no, the cat won! It's a tie!")