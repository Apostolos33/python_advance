rows  = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    action, r, c, value = command.split()
    r, c, value = int(r), int(c), int(value)
    if r in range(0, rows) and c in range(0, rows):
        if action == "Add":
            matrix[r][c] += value
        elif action == "Subtract":
            matrix[r][c] -= value

    else:
        print("Invalid coordinates")

    command = input()
for ls in matrix:
    print(' '.join([str(ch) for ch in ls]))