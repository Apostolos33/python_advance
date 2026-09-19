rows = int(input())

matrix = []

for _ in range(rows):
    cols = [int(x) for x in input().split()]
    matrix.append(cols)

diagonal_sum = 0

for r in range(rows):
    diagonal_sum += matrix[r][r]

print(diagonal_sum)