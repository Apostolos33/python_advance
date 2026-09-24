ROWS = 5
matrix = []
p_r, p_c = 0, 0
targets = 0

for row in range(ROWS):
    curr_row = input().split()
    if "A" in curr_row:
        p_r = row
        p_c = curr_row.index("A")
    matrix.append(curr_row)
    for ch in curr_row:
        if ch == "x":
            targets += 1

n = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

targets_shot = 0
positions_of_targets_shot = []

for _ in range(n):
    if targets == 0:
        break
    command = input().split()
    if command[0] == "move":
        direction, steps = command[1], int(command[2])
        d_r = directions[direction][0] * steps
        d_c = directions[direction][1] * steps
        n_r = p_r + d_r
        n_c = p_c + d_c
        if 0 <= n_r < ROWS and 0 <= n_c < ROWS and matrix[n_r][n_c] == ".":
            matrix[p_r][p_c] = "."
            matrix[n_r][n_c] = "A"
            p_r = n_r
            p_c = n_c

    elif command[0] == "shoot":
        shooting_direction = command[1]
        s_r = directions[shooting_direction][0]
        s_c = directions[shooting_direction][1]
        ps_r = p_r + s_r
        ps_c = p_c + s_c
        while 0 <= ps_r < ROWS and 0 <= ps_c < ROWS:
            if matrix[ps_r][ps_c] == "x":
                targets_shot += 1
                targets -= 1
                positions_of_targets_shot.append([ps_r, ps_c])
                matrix[ps_r][ps_c] = "."
                break
            ps_r += s_r
            ps_c += s_c


if targets:
    print(f"Training not completed! {targets} targets left.")
else:
    print(f"Training completed! All {targets_shot} targets hit.")

for position in positions_of_targets_shot:
    print(position)