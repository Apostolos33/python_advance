def check_row_winner(curr_board, sign):
    for curr_row in curr_board:
        if curr_row.count(sign) >= 3:
            return True
    return False

def check_col_winner(curr_board, sign):
    for c in range(3):
        count = 0
        for r in range(3):
            if curr_board[r][c] == sign:
                count += 1
        if count == 3:
            return True
    return False

def check_diagonal_winner(curr_board, sign):
    prime_diagonal_count = 0
    second_diagonal_count = 0
    for index in range(3):
        if curr_board[index][index] == sign:
            prime_diagonal_count += 1
        if curr_board[index][3 -index -1] == sign:
            second_diagonal_count += 1
    if prime_diagonal_count == 3 or second_diagonal_count == 3:
        return True
    return False

def check_winner(curr_board, sign):
    is_row_winner = check_row_winner(curr_board, sign)
    is_col_winner = check_col_winner(curr_board, sign)
    is_diagonal_winner = check_diagonal_winner(curr_board, sign)
    if is_row_winner or is_col_winner or is_diagonal_winner:
        return True
    return False

def print_board(curr_board):
    for curr_row in curr_board:
        print(f"| {' | '.join(curr_row)} |")


player_one = input("Player one name: ")
player_two = input("Player two name: ")
player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'?").upper()

while player_one_sign not in ["O", "X"]:
    print("Please enter either 'X' or 'O'")
    player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'?").upper()

player_two_sign = "O" if player_one_sign == "X" else "X"

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print(f"{player_one} starts first!")

board = [[" ", " ", " "] for _ in range(3)]
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}
turn = 1

while turn < 10:
    curr_player = player_one if turn % 2 != 0 else player_two
    curr_sign = player_one_sign if turn % 2 != 0 else player_two_sign
    try:
        curr_position = int(input(f"{curr_player} choose a free position [1-9]: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if not (1 <= curr_position <= 9):
        print("Please enter a number between 1 and 9.")
        continue
    row, col = mapper[curr_position]
    if not board[row][col] == " ":
        print("Please enter a free position on the board")
        continue
    board[row][col] = curr_sign
    print_board(board)
    if turn >= 5:
        if check_winner(board, curr_sign):
            print(f"{curr_player} won!")
            break
    turn += 1

if turn > 9:
    print("Its a tie there is no winner today")