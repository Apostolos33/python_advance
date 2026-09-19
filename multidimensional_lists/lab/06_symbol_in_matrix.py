n = int(input())

matrix = []

for _ in range(n):
    col = list(input())
    matrix.append(col)

symbol_to_find = input()
first_occurrence = []

for r in range(n):
    for c in range(n):
        if matrix[r][c] == symbol_to_find:
            first_occurrence.append((r, c))
            print(*first_occurrence)
            exit()

print(f"{symbol_to_find} does not occur in the matrix")