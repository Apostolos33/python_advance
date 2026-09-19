rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for r in range(rows):
    col = [int(x) for x in input().split()]
    matrix.append(col)

for c in range(cols):
    sum_numbers = 0
    for r in range(rows):
        curr_number = matrix[r][c]
        sum_numbers += curr_number
    print(sum_numbers)