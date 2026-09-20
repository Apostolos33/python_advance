rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonals = [matrix[i][i] for i in range(rows)]
secondary_diagonals = [matrix[i][rows - 1 - i] for i in range(rows)]

print(f"{abs(sum(primary_diagonals) - sum(secondary_diagonals))}")