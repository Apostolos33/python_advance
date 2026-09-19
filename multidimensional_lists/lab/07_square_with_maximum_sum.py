rows, cols = [int(x) for x in input().split(", ")]
matrix = []
biggest_number = float("-inf")

for _ in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)

numbers = []

for r in range(rows - 1):
    for c in range(cols -1):
        sum_numbers = 0
        star_number = matrix[r][c]
        right_number = matrix[r][c + 1]
        down_number = matrix[r + 1][c]
        down_right_number = matrix[r + 1][c + 1]
        sum_numbers += star_number + right_number + down_number + down_right_number
        if sum_numbers > biggest_number:
            biggest_number = sum_numbers
            numbers = [[star_number, right_number], [down_number, down_right_number]]

print(*numbers[0])
print(*numbers[1])
print(biggest_number)