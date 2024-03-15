
board = [['[]' for _ in range(3)] for _ in range(3)]  # Initialize board as a list of lists
who_place = 1

def clear_screen():
    for screen in range(0,15):
        print("\033[H\033[J")

def start():
    clear_screen()
    print_board()



def enter():
    global who_place
    col = int(input('What column(1-3): ')) - 1  # Adjusting for zero-based indexing
    row = int(input('What row(1-3): ')) - 1  # Adjusting for zero-based indexing
    if not (0 <= col < 3) or not (0 <= row < 3):
        print("Wrong input. Please enter values between 1 and 3.")
        enter()
    if who_place % 2 != 0:
        who_place += 1
        calculate_x(col, row)
    else:
        who_place += 1
        calculate_y(col, row)


def calculate_y(column, row):
    if board[row][column] == '[]':
        board[row][column] = 'o'
        start()  # Clear and print the board after each move
    else:
        print("This position is already taken. Please choose another.")
        enter()


def calculate_x(column, row):
    if board[row][column] == '[]':
        board[row][column] = 'x'
        start()  # Clear and print the board after each move
    else:
        print("This position is already taken. Please choose another.")
        enter()


def print_board():
    for row in board:
        print(''.join(row))


def tie():
    global game_is_on
    print("tie")
    game_is_on = False


def check_game_status():
    global game_is_on
    if all(cell != '[]' for row in board for cell in row):
        print("It's a tie!")
        game_is_on = False
        return
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '[]':
            print(f"Player {row[0]} wins!")
            game_is_on = False
            return
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '[]':
            print(f"Player {board[0][col]} wins!")
            game_is_on = False
            return
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '[]') or \
       (board[0][2] == board[1][1] == board[2][0] and board[0][2] != '[]'):
        print(f"Player {board[1][1]} wins!")
        game_is_on = False
        return


start()
enter()
game_is_on = True
while game_is_on:
    enter()
    check_game_status()
