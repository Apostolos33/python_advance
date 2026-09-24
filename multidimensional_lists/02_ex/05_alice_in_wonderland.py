n = int(input())

matrix = []

alice_r, alice_c = 0, 0

for row in range(n):
    curr_row = input().split()
    if "A" in curr_row:
        alice_r = row
        alice_c = curr_row.index("A")
    matrix.append(curr_row)

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

bags_of_tea = 0

while bags_of_tea < 10:
    command = input()
    matrix[alice_r][alice_c] = "*"
    d_r = commands[command][0]
    d_c = commands[command][1]
    alice_r += d_r
    alice_c += d_c
    if  0 <= alice_r < n and 0 <= alice_c < n:
        if matrix[alice_r][alice_c] == "R":
            matrix[alice_r][alice_c] = "*"
            print("Alice didn't make it to the tea party.")
            break
        if matrix[alice_r][alice_c] == "." or matrix[alice_r][alice_c] == "*":
            continue

        bags_of_tea += int(matrix[alice_r][alice_c])
        matrix[alice_r][alice_c] = "*"

    else:
        print("Alice didn't make it to the tea party.")
        break

if bags_of_tea >= 10:
    print("She did it! She went to the party.")

for final_row in matrix:
    print(' '.join(final_row))