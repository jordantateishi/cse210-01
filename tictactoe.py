
board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
current_player = "X"
winner = None
game_active = True


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- + - + -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- + - + -")
    print(board[6] + " | " + board[7] + " | " + board[8])

def player_turn(board):
    turn = int(input("Select a spot 1-9: "))
    if board[turn-1] == f'{turn}':
        board[turn-1] = current_player
        


def horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]:
        winner = board[6]
        return True

def row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]:
        winner = board[3]
        return True


def diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4]:
        winner = board[2]
        return True


def check_winner(board):
    global game_active
    if horizontal(board):
        print_board(board)
        print(f"\nThe winner is {winner}")
        game_active = False

    elif row(board):
        print_board(board)
        print(f"\nThe winner is {winner}")
        game_active = False

    elif diagonal(board):
        print_board(board)
        print(f"\nThe winner is {winner}")
        game_active = False


def check_draw(board):
    global game_active
    if "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" not in board:
        print("\nGood game. Thanks for playing!\n")
        game_active = False


def player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



while game_active:
    print_board(board)
    player_turn(board)
    check_winner(board)
    check_draw(board)
    player()



