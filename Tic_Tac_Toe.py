# getting started
from re import X


player_one = input("Player 1, what is your name? ")
player_two = input("Player 2, what is your name? ")

# initial variables
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turns = 0 
player = 1 # keep track of whose turn it is
player_one_symbol = 'X'
player_two_symbol = 'O'

# print starting board 
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print("---------")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
print()

# main game loop
while turns < 9:
    player_one_choice = int(input(f"{player_one}, choose a number to place your {player_one_symbol}: "))
    player_two_choice = int(input(f"{player_two}, choose a number to place your {player_two_symbol}: "))

    # locate where to place symbol for player one
    if player_one_choice == 1:
        board[0][0] = player_one_symbol
    elif player_one_choice == 2:
        board[0][1] = player_one_symbol
    elif player_one_choice == 3:
        board[0][2] = player_one_symbol
    elif player_one_choice == 4:
        board[1][0] = player_one_symbol
    elif player_one_choice == 5:
        board[1][1] = player_one_symbol
    elif player_one_choice == 6:
        board[1][2] = player_one_symbol
    elif player_one_choice == 7:
        board[2][0] = player_one_symbol
    elif player_one_choice == 8:
        board[2][1] = player_one_symbol
    elif player_one_choice == 9:
        board[2][2] = player_one_symbol
    else:
        print("invalid choice")

    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print()

    turns += 1
    
    # locate where to place symbol for player two
    if player_two_choice == 1:
        board[0][0] = player_two_symbol
    elif player_two_choice == 2:
        board[0][1] = player_two_symbol
    elif player_two_choice == 3:
        board[0][2] = player_two_symbol
    elif player_two_choice == 4:
        board[1][0] = player_two_symbol
    elif player_two_choice == 5:
        board[1][1] = player_two_symbol
    elif player_two_choice == 6:
        board[1][2] = player_two_symbol
    elif player_two_choice == 7:
        board[2][0] = player_two_symbol
    elif player_two_choice == 8:
        board[2][1] = player_two_symbol
    elif player_two_choice == 9:
        board[2][2] = player_two_symbol
    else:
        print("invalid choice")

    turns += 1

    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print()

    # determine next player 
    if player == 1:
        player = 2
    else:
        player = 1
print("Game over")

    
