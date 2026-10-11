class InvalidColError(Exception):
    pass

class FullColError(Exception):
    pass

def is_player_num(ma, r, c, player):
    if (0 > r or r >= len(ma)) or (0 > c  or c >= len(ma[0])):
        return False
    return ma[r][c] == player

def create_matrix(r, c):
    ma = [[0 for _ in range(c)] for _ in range(r)]
    return ma

def print_matrix(ma):
    for m in ma:
        print(m)

def is_valid_col(num, cols):
    if not (0 <= num < cols):
        raise InvalidColError

def place_player_choice(ma, c, player):
    for r in range(len(matrix)-1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player
            return r, c
    raise FullColError

def is_col_winner(ma, r, c, player, slots):
    return all(is_player_num(ma, r + idx, c, player) for idx in range(slots))

def is_row_winner(ma, r, c, player, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, player):
            filled += 1
        else:
            break
    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, player):
            filled += 1
        else:
            break
    return filled >= slots


def is_right_diagonal_winner(ma, r, c, player, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player):
            filled += 1
        else:
            break
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player):
            filled += 1
        else:
            break
    return filled >= slots

def is_left_diagonal_winner(ma, r, c, player, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player):
            filled += 1
        else:
            break
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player):
            filled += 1
        else:
            break
    return filled >= slots

def is_winner(ma, r, c, player, slots):
    if is_row_winner(ma, r, c, player, slots) or is_col_winner(ma, r, c, player, slots) or is_left_diagonal_winner(ma, r, c, player, slots) or is_right_diagonal_winner(ma, r, c, player, slots):
        return True
    return False

ROWS = 6
COLS = 7
SLOTS = 4

matrix = create_matrix(ROWS, COLS)
player_one = 1
player_two = 2
turn = 1

while True:
    curr_player = player_one if turn % 2 != 0 else player_two
    try:
        choose_a_col = int(input(f"Player {curr_player}, please choose a column\n ")) -1
        is_valid_col(choose_a_col, COLS)
        row, col = place_player_choice(matrix, choose_a_col, curr_player)

    except ValueError:
        print("Please enter a valid value")
        continue
    except InvalidColError:
        print("Please enter a valid col from 1 to 7")
        continue
    except FullColError:
        print("This col is full please select another")
        continue
    if is_winner(matrix, row, col, curr_player, SLOTS):
        print(f"Plyer {curr_player} won the game")
        print_matrix(matrix)
        break

    print_matrix(matrix)
    turn += 1

    if turn >= ROWS * COLS:
        print("Its a tie")
        break