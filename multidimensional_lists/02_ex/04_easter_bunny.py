n = int(input())

matrix = []
bunny = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
bunny_r, bunny_c = 0, 0

for row in range(n):
    curr_row = input().split()
    if "B" in curr_row:
        bunny_r = row
        bunny_c = curr_row.index("B")

    matrix.append(curr_row)

best_direction = ""
best_path = []
max_eggs = -float("inf")

for direction, move in directions.items():
    curr_r = bunny_r + move[0]
    curr_c = bunny_c + move[1]
    eggs = 0
    curr_path = []

    while 0 <= curr_r < n and 0 <= curr_c < n:
        if matrix[curr_r][curr_c] == "X":
            break

        eggs += int(matrix[curr_r][curr_c])
        curr_path.append([curr_r, curr_c])
        curr_r += move[0]
        curr_c += move[1]

    if eggs > max_eggs and curr_path:
        max_eggs = eggs
        best_direction = direction
        best_path = curr_path

print(best_direction)
for path in best_path:
    print(path)
print(max_eggs)