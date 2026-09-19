rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_cols = 0

for r in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)
    sum_cols += sum(col)

print(sum_cols)
print(matrix)