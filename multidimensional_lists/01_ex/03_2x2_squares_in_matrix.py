rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

squares_containing_identical_chars = 0

for r in range(rows -1):
    for c in range(cols -1):
        first_char = matrix[r][c]
        right_char = matrix[r][c+1]
        down_char = matrix[r+1][c]
        down_right_char = matrix[r+1][c+1]
        if first_char == right_char and first_char == down_char and first_char == down_right_char:
            squares_containing_identical_chars += 1

print(squares_containing_identical_chars)