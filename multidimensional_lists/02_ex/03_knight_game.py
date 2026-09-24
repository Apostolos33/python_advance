n = int(input())

matrix = []

knights = []

knight_moves = [[-1, -2], [-2, -1], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1] ]


for row in range(n):
    curr_col = list(input())
    for col in range(n):
        if curr_col[col] == "K":
            knights.append([row, col])
    matrix.append(curr_col)

knights_removed = 0

while True:
    max_knights_attacks = 0
    max_knight = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                current_knight_attacks = 0

                for move in knight_moves:
                    n_r = row + move[0]
                    n_c = col + move[1]

                    if 0 <= n_r < n and 0 <= n_c < n and matrix[n_r][n_c] == "K":
                        current_knight_attacks += 1

                if current_knight_attacks > max_knights_attacks:
                    max_knights_attacks = current_knight_attacks
                    max_knight = [row, col]

    if max_knights_attacks == 0:
        break
    matrix[max_knight[0]][max_knight[1]] = "0"
    knights_removed += 1

print(knights_removed)