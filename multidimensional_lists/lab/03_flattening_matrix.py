rows = int(input())

matrix = []

for _ in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.extend(col)

print(matrix)