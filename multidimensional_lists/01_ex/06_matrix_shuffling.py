def is_valid_command(r1, c1, r2, c2, rows, col):
    return 0 <= r1 < rows and 0 <= c1 < col and 0 <= r2 < rows and 0 <= c2 < col

r, c = map(int, input().split())

matrix = [[x for x in input().split()] for _ in range(r)]

while True:
    command = input()


    if command == "END":
        break
    command_list = command.split()

    if len(command_list) != 5 or command_list[0] != "swap":
        print("Invalid input!")
        continue
    r_1, c_1, r_2, c_2 = [int(x) for x in command_list[1:]]
    if is_valid_command(r_1, c_1, r_2, c_2, r, c):
        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
        for row in matrix:
            print(*row)
    else:
        print("Invalid input!")